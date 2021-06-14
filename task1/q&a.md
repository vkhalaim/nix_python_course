# Написать Linux-команды для следующих вопросов:

### Как посмотреть содержимое текстового файла?
`cat filename`
### Что делает команда tail? Как посмотреть?
`tail filename` - Print the last 10 lines of each FILE to standard output.

`man tail` - The system's manual pager 
### Как посмотреть текущую рабочую директорию?
`pwd`
### Как сменить рабочую директорию?
`cd`
### Как перейти в родительскую директорию?
`cd ..`
### Как вернуться в домашнюю директорию?
`cd ~`
### Как вывести список файлов в директории?
`ls`
### Как посмотреть вермя последнего изменения/доступа к файлу /tmp/test.txt?
`stat /tmp/test.txt`
### Как создать новую директорию test?
`mkdir test`
### Как создать пустой файл?
`touch filename`
### Как создать файл /tmp/2mb.txt размером 2Mb?
`truncate -s 2M /tmp/2mb.txt`
### Как узнать тип файла?
`file filename`
### Как переименовать файл?
`mv filename new_filename`
### Как удалить файл/директорию?
`rm filename` - removes file

`rmdir dirname` - removes empty dir

`rmdir -r dirname` - removes non-empty link
### Как создать символическую/жесткую ссылку на файл/директорию?
`ln filename hardlink_name` - hardlink

`ln -s filename hardlink_name` - symbolic link
### Как посмотреть размер файла?
`ls -sh filename`
### Как как узнать размер директории?
`ls -sh dirname`
### Как сравнить два текстовых файла?
`diff filename1 filename2`
### Как посчитать количество строк в текстовом файле?
`wc -l filename`
### Как вывести на экран отсортированные строки текстового файла?
`sort filename`