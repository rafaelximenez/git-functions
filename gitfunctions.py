from git import Repo


class Git:
    def __init__(self, remote_repository_name='origin', repo_path='.'):
        self.repository = Repo(repo_path)
        self.remote_repository_name = remote_repository_name


    def __remote_repository_exists(self):
        try:             
            remote = self.repository.remote(remote_repository_name)
            remote.fetch()
            latest_remote_commit = remote.refs[self.repository.active_branch.name].commit

            return latest_remote_commit, True
        except:            
            return None, False


    def check_updates(self):
        latest_local_commit = self.repository.head.commit
        latest_remote_commit, remote_repository_exists = self.__remote_repository_exists()

        print(f"Mudanças não commitadas ou unstaged: {self.repository.is_dirty()}")
        print(f"Arquivos untracked: {len(self.repository.untracked_files)}")

        if remote_repository_exists: print(f'Sem repositório remoto: {remote_repository_name}')
        
        print(f"Último commit enviado: {latest_local_commit == latest_remote_commit}")