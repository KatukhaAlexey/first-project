# ��������� �� ������ � GIT �� ������� � ���� ��������<br>
## ��������� ������<br>
<br>
__ pwd __ - �� ����. _print working directory_ - "�������� ������� �����". ������� ���� � ������� ����������.<br>
**cd** - �� ����. _change directory_ - "������� ����������". ������� ��� �������� ����� ������������. **~** - ����������� �������� ����������. ���� ���� � ���������� �������� �������, ��� ����� ��������� � �������. **.** - ������� ����������. **..** - ������������ ����������.<br>
**ls** - �� ����. _list directory contents_ - "���������� ���������� ����������". **ls -s** - ������� ����������� ������. � ��� ����������� ��� ������� �����, ������� ���������� � ".".<br>
**touch** - ������� ��� �������� �����, � ������ ����� � �������� ���������<br>
**mkdir** - �� ����. _makr directory_ - "������� ����������". ����� ������� ����� ��������� ���������� ����� �������� � ������� ����� **-p**.<br>
**mkdir -p dir1/dir2/dir3** - ������� ��������� ����������, ��������� ���� � �����.<br>
**cp** - �� ����. _copy_ - "����������". ������� ��� ����������� ������. � �������� ���������� ����������� ��� ���������� � ���� ����������. ����� ������� ����� ��������� ������.<br>
**mv** - �� ����. _move_ - "�����������". ����� ����� ������� ��������� ������ ������ � �����, ������� ����� �����������, � ����� - �����, � ������� ����� ��������� �����������.<br>
**cat** - �� ����. _concatenate and print_ - "���������� � �����������". ������� ��������� ���� � �������. ������� �������� ������ � ���������� �������.<br>
**rm** - �� ����. _remove_ - "�������". ������� ������� ����. ���� **-r** - �� ����. _recursive_ - "�����������" ��������� ������� ����� � �������<br>
**rmdir** �� ����. _remove directory_ - "������� ����������". ������� ������� ����������, �� ��� ������ ���� ������.<br>
<br>
������� � ��������� ����� ��������� �� �� �����, � ����� �������. ��� ����� �� ����� ��������� ����� ������������ **&&**.<br>
<br>
���� ����� ����� �������� �����-���� �������, ���������� ���������, � ����� ���� ��� ���������� � ������ ������ **Tab**. **Tab** �� ������ ���������� �������, �� � ����.<br>

---

## ������� Git<br>
<br>
**git version** - ������� ������ ������� ������ �������������� Git<br>
**git config --global user.name "User Ivanov"**<br>
**git config --global user.email user@yandex.ru**<br>
� ���������� Git ��������� ���� ��� (���������) � ���� ����������� �������� ����.<br>
��� ���������� ��������� Git ������ � ����� **.gitconfig** � �������� ����������.<br>
**git config --list** - ������� ���������� ����� Git<br>
**git init** - ������� ������� ����� ������������. � ������� ���������� ��������� ���������� ".git", � ������� ����� �������� ��������� ����������. <br>
"���������" ����� ����� ��������� ���� ����������. � ������� ��������� ������� **rm -rf .git**. **f** �������� ������� �� ������������� �������� ������.<br>
**git status** - �������� ������� ��������� �����������<br>
**git add** - �������������� ����� � ���������� � �����������. ����� ���� ������� ���������� ������� ���� (�����). ���� **--all** ��������� ����������� � ���������� ��� �����.<br>
**git commit -m '���������� � �������' - ������� ������ � ������ -m, ������� ����������� ������� ���������. ��������� ������� � ��������.<br>
**git log** - ������� ������� � �������� ��������������� �������.<br>
**git log --online** - ����������� ���.
<br>
��� ��������� SSH-���� ������ ������������ ��������� **ssh-keygen**.<br>
**ssh-keygen -t ed25519 -C "����������� �����, � ������� �������� ��� ������� �� GitHud"<br>
� ������ ������������� ������ ���������� ������������ ������ �������� ����������.<br>
**ssh-keygen -t rsa -b 4096 -C "����������� �����, � ������� �������� ��� ������� �� GitHud"<br>
**clip < ~/.ssh/id_rsa.pub** ��� **clip < ~/.ssh/id_ed25519.pub** - ����������� ����������� ����� �� ������� � ����� ������.<br>
**ssh -T git@github.com** - ��������� ������������ �����.<br>
<br>
��� ����, ����� ��������� ��������� ����������� � ���������� ���������� ������� � ���������� ����������� � ��������� �������:<br>
**git remote add origin git@github.com:%���_��������%/%���_�������%.git<br>
������� ���������� �������� ��� ���������: ��� ���������� ����������� � ��� URL. � �������� ����� ����������� ��� origin, � URL ����������� �� �������� ���������� �����������.<br>
**git remote -v** - ��������, ��� ��������� ����������� ������ � ���������. � ������ ������ ���� ��� �������.<br>
**git push** - ��������� ���������� ���������� ����������� �� GitHub. ������ ��� ��� ������� ����� ������� � ������ **-u** � ���������� **origin** � **main** ��� **master**. ���� **-u** ������ ��������� ����� � ����������� ���������.<br>

---

HEAD -- ��� ������.
������ -- ��� ����� ������.
������� ������:
<br>
<br>
'''
<br>
mermaid
<br>
graph LR;
<br>
untracked -- "git add" --> staged;
<br>
staged -- "???" --> tracked/comitted;
<br>
%% ������� ��� ������ ��� �������:
<br>
A --> B;
<br>
%% �������� �����
<br>
'''
<br>
<br>

