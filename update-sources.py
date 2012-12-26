#!/usr/bin/env python

import sys

# We use argparse, which is available from python 2.7 onwards
if sys.hexversion < 0x2070000:
    sys.exit('Python v2.7 or later required')

# XXX: should probably check for < 3.0 too thanks to print/print()


# The will be populated with the stored commit id's
QT5_ESSENTIAL_MODULES = {
    'qtbase'        :   None,
    'qtjsbackend'   :   None,
    'qtdeclarative' :   None,
    'qtmultimedia'  :   None,
    'qtwebkit'      :   None,
    }
QT_ADDON_MODULES = {
    'qtimageformats':   None,
    'qtscript'      :   None,
    'qtquick1'      :   None,
    'qtlocation'    :   None,
    'qtgraphicaleffects':None,
    'qtsvg'         :   None,
    'qttools'       :   None,
    'qtxmlpatterns' :   None,
    'qtwayland'     :   None
    }
# All together now
QT5_MODULES = {}
QT5_MODULES.update(QT5_ESSENTIAL_MODULES)
QT5_MODULES.update(QT_ADDON_MODULES)


import os
import subprocess
import shutil
import argparse
import datetime
import tempfile
import glob

class Qt5HelperError(Exception):
    def __init__(self, msg=None):
        if msg:
            print '\n%s\n' % msg

# Idea of this class is that all external commands may be generated via
# a single helper. The resulting code should be more readable - and a
# LOT easier to maintain.
class CommandHelper(object):
    def __init__(self):
        self.QT5_DIR = None
        self.OBS_DIR = None
        self.OSC_OPT = None
        self.options = None
        self.scriptdir = os.path.dirname(os.path.abspath(__file__))

    def setup(self, script_opts):
        # These raise key error if variable not set
        self.QT5_DIR = os.environ['QT5_DIR']
        self.OBS_DIR = os.environ['OBSDIR']
        #
        # dict.get() can return None without error
        self.OSC_OPT = os.environ.get('OSC_OPTS')
        #
        # Changelog entries
        self.GIT_AUTHOR = os.environ.get('GIT_AUTHOR_NAME')
        self.GIT_EMAIL = os.environ.get('GIT_AUTHOR_EMAIL')
        #
        self.options = script_opts

    def __osc_opt(self):
        if self.OSC_OPT:
            return self.OSC_OPT
        return ''

    def osc(self):
        cmd = ['osc', self.__osc_opt()]
        return cmd

    def osc_update(self, module):
        c = self.osc()
        c.extend(['update', module])
        return c

    # NOTE: 'modulepaths' is always a list of paths to OBS packages
    def osc_commit(self, modulepaths):
        c = self.osc()
        c.extend(['commit', '-m', 'automated source upload'])
        c.extend(modulepaths)
        return c

    def osc_addremove(self, module):
        c = self.osc()
        c.extend(['addremove', module])
        return c

    # NOTE: This can be a no-op depending on options
    def update_changelog(self, module, version):
        # By keeping this here, the final logic code will be simpler
        if not self.options['update_changelog']:
            return
        #
        # Force datetime conversion to use correct locale
        orig_lc_time = os.environ.get('LC_TIME')
        os.environ['LC_TIME'] = 'C'
        t = datetime.datetime.now()
        if orig_lc_time is not None:
            os.environ['LC_TIME'] = orig_lc_time
        date_str = t.strftime('%a %b %d %Y')

        fname = ''
        # QtWebKit has a trailing '5' in filenames
        if module == 'qtwebkit':
            fname = '%s5.changes' % module
        else:
            fname = '%s.changes' % module
        p = os.path.join(self.OBS_DIR, module, fname)

        # Changelog entry
        hdr = '%s %s <%s> - %s' % (date_str, self.GIT_AUTHOR,
                self.GIT_EMAIL, version)
        entry = [hdr, '- Automated source update', '']
        # Generate new, add to top
        tmpf = tempfile.NamedTemporaryFile(suffix='.changes')
        for l in entry:
            tmpf.write(l + '\n')
        if os.path.exists(p):
            oldf = open(p, 'r')
            for line in oldf:
                tmpf.write(line)
            oldf.close()
        tmpf.flush()
        shutil.copy(tmpf.name, p) # Copy tempfile to original path
        tmpf.close() # Automatically removed here

    # This should NEVER be a no-op
    def update_spec(self, module, version):
        # QtWebKit has a trailing '5' in filenames
        specfile = ''
        if module == 'qtwebkit':
            specfile = '%s5.spec' % module
        else:
            specfile = '%s.spec' % module
        specpath = os.path.join(self.scriptdir, module, specfile)
        tgtpath = os.path.join(self.OBS_DIR, module, specfile)
        #
        # Generate modified spec and copy it out to OBS dir
        tmpf = tempfile.NamedTemporaryFile(suffix='.spec')
        f = open(specpath, 'r')
        for line in f:
            if line.find('_qtmodule_snapshot_version') > 0:
                tmpf.write(line.replace('%nil', version))
            else:
                tmpf.write(line)
        f.close()
        tmpf.flush()
        shutil.copy(tmpf.name, tgtpath) # Copy to _target_ path
        tmpf.close() # Automatically removed here

    # This can be a no-op
    def copy_extra_files(self, module):
        _dir = os.path.join(self.scriptdir, module, 'files')
        if not os.path.exists(_dir):
            return
        print '\t+ additional packaging files for Qt5/%s' % module
        extra_files = glob.glob(_dir + '/*')
        for f in extra_files:
            fname = os.path.basename(f)
            tgt_path = os.path.join(self.OBS_DIR, module, fname)
            shutil.copyfile(f, tgt_path)

    def update_package_state(self, module):
        _dir = os.path.join(self.OBS_DIR, module)
        os.chdir(_dir)
        osc_cmd = self.osc_addremove(module)
        subprocess.check_call(osc_cmd)
        os.chdir(self.scriptdir)


    # Before operating on Qt5 modules, we want to make sure the contents
    # of the OBS packages are up to date
    def checkout_current_obs_package(self, module):
        print 'OBS package: %s' % module
        p = os.path.join(self.OBS_DIR, module)
        _osc = os.path.join(p, '.osc')
        if not os.path.exists(_osc):
            raise Qt5HelperError('Module %s at "%s" is not a ' +
                    'valid OBS package' % (module, p))
        os.chdir(self.OBS_DIR)
        osc_cmd = self.osc_update(module)
        subprocess.check_call(osc_cmd)
        os.chdir(self.scriptdir)

    def commit_obs_packages(self, modules):
        modulepaths = []
        for m in modules:
            p = os.path.join(self.OBS_DIR, m)
            modulepaths.append(p)
        # osc_commit() runs with full paths
        osc_cmd = self.osc_commit(modulepaths)
        subprocess.check_call(osc_cmd)






class GitCommandHelper(CommandHelper):
    def __init__(self):
        CommandHelper.__init__(self)
        self.git_ref = None
        self.revision = None
        self.module_revisions = dict()
        self.revdir = os.path.join(os.path.expanduser('~'),
            '.modular-qt5-revs')
        self.__last_archived()

    def setup(self, opts):
        CommandHelper.setup(self, opts)
        if self.options['force_upload']:
            self.__purge_stored_revs()
        #
        # Use the gitref version
        _ref = self.options.get('gitref')
        self.git_set_version(_ref)
        #
        # And if provided, use override version string
        if self.options['forced_version']:
            self.git_override_version(self.options['forced_version'])


    def __get_current_git_revs(self):
        for m in self.options['modules']:
            p = os.path.join(self.QT5_DIR, m)
            if not os.path.exists(p):
                # XXX: error out on non-existent module?
                continue
            os.chdir(p)
            self.module_revisions[m] = self.__get_git_ref(m)

    def __purge_stored_revs(self):
        revs = glob.glob('%s/*' % self.revdir)
        for r in revs:
            os.remove(r)
        # clear revs from memory too
        for m in QT5_MODULES:
            QT5_MODULES[m] = None


    def __stored_rev(self, fp):
        f = open(fp, 'r')
        rev = f.readline().strip()
        f.close()
        return rev

    def __last_archived(self):
        if not os.path.exists(self.revdir):
            os.mkdir(self.revdir)
            return
        # There may be files
        for _mod in QT5_MODULES:
            p = os.path.join(self.revdir, _mod)
            if not os.path.exists(p):
                continue
            QT5_MODULES[_mod] = self.__stored_rev(p)

    def __put_last_archived(self, modname, ref):
        if not os.path.exists(self.revdir):
            os.mkdir(self.revdir)
            return
        p = os.path.join(self.revdir, modname)
        f = open(p, 'w')
        f.write(ref + '\n')
        f.close()

    def __remove_old_tarballs(self, modname=None):
        if modname is None:
            raise Qt5HelperError('module name not specified')
        p = os.path.join(self.OBS_DIR, modname)
        files = glob.glob('%s/*.tar.*' % p)
        for f in files:
            os.remove(f)

    def __generate_tarball(self, modname=None):
        if self.git_ref is None:
            raise Qt5HelperError('git ref unset, call .git_set_version()?')
        if modname is None:
            raise Qt5HelperError('module name not specified')

        # XXX: --module-gitref overrides normal behaviour
        _arc_ref = 'HEAD'
        if self.options['module_gitref']:
            _arc_ref = self.options['module_gitref']
            print 'Using "%s" as gitref for %s' % (_arc_ref, modname)
        #
        print 'Balling up Qt5/%s ...' % modname
        # Pipe: "git-archive .. | gzip > tarball"
        git_cmd = ['git', 'archive',
                '--format=tar',
                '--prefix=qt5-%s/' % modname,
                _arc_ref]
        gz_cmd  = ['gzip', '-']

        out_file_name = 'qt5-%s-%s.tar.gz' % (modname, self.revision)
        out_path = os.path.join(self.OBS_DIR, modname, out_file_name)
        out_dir = os.path.join(self.OBS_DIR, modname)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        # Note: tarball path is TRUNCATED
        f = open(out_path, 'w')
        git_proc = subprocess.Popen(git_cmd, stdout=subprocess.PIPE)
        gz_proc = subprocess.Popen(gz_cmd, stdin=git_proc.stdout, stdout=f)
        git_proc.stdout.close() # SIGPIPE handling
        gz_proc.communicate()
        f.close()

    def __git_ref_for(self, modname=None):
        if modname is None:
            raise Qt5HelperError('No module specified!')
        p = os.path.join(self.QT5_DIR, modname)
        if not os.path.exists(p):
            raise Qt5HelperError('Invalid Qt5 git module path: %s' % p)
        os.chdir(p)
        return self.__get_git_ref(modname)


    def __do_git_fetch(self):
        subprocess.check_call([
            'git',
            'fetch'])

    def __do_checkout_umbrella_ref(self):
        print 'Checking out "%s" in qt5.git' % self.git_ref
        subprocess.check_call([
            'git',
            'checkout',
            self.git_ref])

    def __do_checkout_submodules(self):
        print 'Updating submodules...'
        subprocess.check_call([
            'git',
            'submodule',
            'sync'])
        subprocess.check_call([
            'git',
            'submodule',
            'update'])

    # We try to checkout the given ref (stored in .git_ref), but if that
    # particular checkout fails, we revert to origin/master. Reason for
    # using origin/ is that local master *could* theoretically have
    # extra commits.
    #
    # Qt5 git trees are fragile enough as they are, there's no need to
    # introduce any further complications if we can avoid it.
    def __checkout_ref(self):
        os.chdir(self.QT5_DIR)
        try:
            self.__do_checkout_umbrella_ref()
        except subprocess.CalledProcessError:
            print 'qt5.git does not have ref "%s"'
            print 'Reverting to origin/master ...'
            self.git_ref = 'origin/master'
            self.__do_checkout_umbrella_ref()
        finally:
            self.__do_checkout_submodules()
            # Get module heads
            self.__get_current_git_revs()
        os.chdir(self.scriptdir)


    # NOTE: this is called when we are already inside a module dir
    def __get_git_ref(self, module):
        commit = subprocess.check_output(['git', 'show', 'HEAD'])
        lines = commit.split('\n') # -sigh-
        # If the commit is a merge, the actual 'commit $SHA1' may be
        # anywhere, so we can't shortcircuit to just first line
        for line in lines:
            if not line.startswith('commit'):
                continue
            (_c, sha1) = line.strip().split()
            break
        return sha1

    # The literal SHA1 for currently checked out HEAD
    # NOTE: this is called when we are already inside a module dir
    def __store_git_ref(self, module):
        QT5_MODULES[module] = self.__get_git_ref(module)


    def __revision_from_git_describe(self, gd):
        rev = ''
        parts = gd.split('-')
        if len(parts) == 4:
            _githash = parts.pop()
            _count = parts.pop()
            _extra = parts.pop()
            _version = parts.pop()
            rev = '%s~%s+%s-%s' % (_version, _extra, _count, _githash)
        elif len(parts) == 3:
            _githash = parts.pop()
            _count = parts.pop()
            _version = parts.pop()
            rev = '%s+%s-%s' % (_version, _count, _githash)
        elif len(parts) < 3:
            raise Qt5HelperError('Unknown qt5.git revision: "%s"', gd)
        return rev

    def __generate_git_revision(self):
        os.chdir(self.QT5_DIR)
        rev = subprocess.check_output(['git', 'describe', 'HEAD'])
        rev = rev.strip()
        self.revision = self.__revision_from_git_describe(rev)
        os.chdir(self.scriptdir)

    # Write the just archived git SHA1 to stored revisions
    # NOTE: ref has been updated at __store_git_ref()
    def update_archived(self, module):
        _ref = QT5_MODULES[module]
        if _ref is None:
            raise Qt5HelperError('invalid ref (%s) for %s' % (_ref, module))
        self.__put_last_archived(module, _ref)


    # This sets the used git commit. The 'ref' must be usable by
    # git-checkout, so it must be one the following:
    #   - tag
    #   - branch name
    #   - git commit SHA1 string
    # If the named ref can not be found in qt5.git, the used 'ref' will
    # revert back to 'origin/master'
    def git_set_version(self, ref=None):
        if ref is None:
            self.git_ref = 'origin/master'
        else:
            self.git_ref = ref
        #
        _pull = self.options.get('pull')
        if _pull:
            self.__do_git_fetch()
        self.__checkout_ref()
        self.__generate_git_revision()

    def git_override_version(self, force_name=None):
        self.revision = force_name

    # Generate a tarball from given module
    def git_tarball_module(self, modname=None):
        if modname not in QT5_MODULES:
            raise Qt5HelperError('Unknown module "%s"' % modname)
        modpath = os.path.join(self.QT5_DIR, modname)
        os.chdir(modpath)
        self.__remove_old_tarballs(modname)
        self.__generate_tarball(modname)
        self.__store_git_ref(modname)

    # Very high-level logic for generating files for OBS upload
    def run(self):
        if self.revision:
            version_str = self.revision
        else:
            version_str = 'No-can-do'

        # Get all modules we want to work on up-to-date first
        if self.options['update_obs']:
            print 'Updating to most recent OBS packages...'
            for m in self.options['modules']:
                self.checkout_current_obs_package(m)

        # Update OBS package contents
        for m in self.options['modules']:
            if not self.module_revisions.has_key(m):
                print 'Skipping module: %s' % m
                continue
            if self.module_revisions[m] != QT5_MODULES[m]:
                self.git_tarball_module(m)
                self.update_archived(m)
            # These are unconditional attempts, so we can upload
            # spec-only changes
            self.update_changelog(m, version_str)
            self.update_spec(m, version_str)
            self.copy_extra_files(m)
            self.update_package_state(m)

        # Commit all packages in a single batch upload
        self.commit_obs_packages(self.options['modules'])




# We don't want to pollute actual code logic with any option parsing
class CommandLineArgs(object):
    def __init__(self):
        self._HELPTEXT = """
Generate and upload Qt5 tarballs to OBS for automated building.

Requires the following environment variables to be set:
    QT5_DIR:    path where qt5.git is cloned
    OBSDIR:     path to Qt5 OBS project

Uses the following environment variables if they are set:
    OSC_OPTS:   global 'osc' arguments

"""
        self.parser = argparse.ArgumentParser(description=self._HELPTEXT,
            formatter_class=argparse.RawDescriptionHelpFormatter)
        #
        self.__setup_arg_options()

    def __setup_arg_options(self):
        self.parser.add_argument('--pull', help='Force git pull',
                action='store_true', dest='pull')
        self.parser.add_argument('--no-pull', help='Prevent git pull (default)',
                action='store_false', dest='pull', default=False)
        self.parser.add_argument('--force-upload', help='Force tarball upload',
                action='store_true', dest='force', default=False)
        self.parser.add_argument('--override-version', help='Use as version string',
                action='store', dest='forced_version', default=None)
        # If gitref==None, we will later assume qt5.git:master
        self.parser.add_argument('--gitref', help='Use named ref for source version',
                action='store', dest='gitref', default=None, type=str)
        self.parser.add_argument('--module',
                help='Update specified module only. May be given \
                multiple times for additional modules.',
                action='append', dest='modules', default=None, type=str)
        # *IF* we for some reason need to use a specific in-module
        # gitref (when qt5.git is out of date), this option allows to
        # set the 'ref' for git-archive.
        # XXX: if this option is set, there must be exactly one module
        self.parser.add_argument('--module-gitref',
                help='Use ref for given module. Overrides umbrella repo gitref.',
                action='store', dest='module_gitref', default=None,
                type=str)
        # Creation of changelog can be toggled off
        self.parser.add_argument('--skip-changelog', help='Do not update changelog',
                action='store_false', dest='bump_changelog', default=True)
        # Toggle "osc update"
        self.parser.add_argument('--skip-osc-update',
            help='Do not checkout current OBS packages (dangerous)',
            action='store_false', dest='update_osc_pkgs', default=True)
        # Use tarballs instead of git
        self.parser.add_argument('--tarball',
                help='Use existing tarball(s). Requires --module (not implemented)',
                action='store', dest='tarball_path', default=None)


    def __check_module_names(self, modules):
        wrong = []
        for m in modules:
            if m not in QT5_MODULES:
                wrong.append(m)
        if wrong:
            raise Qt5HelperError('Unknown module(s) specified: %s' % wrong)


    # We want to limit the visibility of parser, so sanitize the given
    # options here and expose runtime options via a simple dictionary
    def __sanitized(self, opts):
        cleaned = dict()
        #
        # Start with --module-gitref, it's fragile
        if opts.module_gitref:
            print 'NOTICE: module-specific gitref specified'
            if len(opts.modules) != 1:
                raise Qt5HelperError('Using --module-gitref' +
                    ' requires EXACTLY one module')
            cleaned['module_gitref'] = opts.module_gitref
        # Manually set modules override defaults
        if opts.modules:
            self.__check_module_names(opts.modules)
            cleaned['modules'] = opts.modules
        else:
            cleaned['modules'] = QT5_MODULES
        #
        if opts.gitref:
            cleaned['gitref'] = opts.gitref
        #
        # Override version string (may be None)
        cleaned['forced_version'] = opts.forced_version
        #
        # Force and pull toggle are copied directly
        cleaned['pull'] = opts.pull
        cleaned['force_upload'] = opts.force
        #
        # Changelog
        cleaned['update_changelog'] = opts.bump_changelog
        #
        # OBS package sync at start
        cleaned['update_obs'] = opts.update_osc_pkgs
        #
        # FIXME: tarball handling not implemented
        #
        return cleaned


    def parse(self):
        options = self.parser.parse_args()

        # Specified modules override default list
        modules = options.modules
        if modules is None:
            modules = QT5_MODULES

        # Returns a dict
        return self.__sanitized(options)






if __name__ == '__main__':
    cla = CommandLineArgs()
    script_options = cla.parse()

    g = GitCommandHelper()
    g.setup(script_options)

    g.run()

