from fabric.api import local

def test():
  local("cd /opt/python/fabtest/fab_test && touch file1 file2 file3")
  local("cd /opt/python/fabtest/fab_test && git add . && git commit -m test")
  local("cd /opt/python/fabtest/fab_test && git push origin master")
