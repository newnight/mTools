# coding=utf8
 
import sublime,sublime_plugin,os


class ToolsCommand(sublime_plugin.WindowCommand):
    __first_path=''
    __sec_path=''
    _source=''

    # todo: 读取配置
    __cmd ='/usr/local/bin/bcompare' if os.path.exists('/usr/local/bin/bcompare') else ''

    def get_path(self,is_folder=False):
        path = self.window.active_view().file_name()
        if is_folder:
            path=os.path.dirname(path)

        return path

    def set_path(self,target,is_folder):
        self.__first_path=self.get_path(is_folder)
        self.__sec_path=self.__first_path.replace(self._source,target)

    def runCmd(self,target,is_folder):
        self.set_path(target,is_folder)
        if self._source!=target:
            import subprocess
            subprocess.Popen([self.__cmd,self.__first_path,self.__sec_path])

    def set_source(self):
        path = self.get_path()
        if 'rc' in path:
            self._source='rc'
        elif 'dev' in path:
            self._source='dev'
        elif 'dev2' in path:
            self._source='dev2'
        elif 'local_view' in path:
            self._source='local_view'

    def is_visible(self,target=''):
        self.set_source()
        return self.__cmd!='' and self._source!=''

class BcompareWithCommand(ToolsCommand):
    def run(self,target):
        # is_folder 读取配置
        is_folder=True
        self.runCmd(target,is_folder);

    def is_visible(self,target):
        self.set_source()
        return super().is_visible() and self._source!=target

