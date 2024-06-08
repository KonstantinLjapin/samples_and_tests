declare -A checksumap
declare -A extensionsmap

#Функция для получения счётчика контрольной суммы
get_checksum_double(){
  echo -e "\033[35m Double checksum:"
  for i in ${!checksumap[*]}
    do
    if [[ ${checksumap[$i]} == *[',']* ]]; then
      echo "$i:"
      echo ${checksumap[$i]} | tr "," "\n"
    fi

    done
}

#Функция для получения счётчика расширений
get_count_extensions(){
  echo -e "\033[32m Count extension: "
  for i in ${!extensionsmap[*]}
    do
    echo "$i = ${extensionsmap[$i]}"
    done
}

#Функция для записи расширения
post_extensions(){
  local extension="$1"
    # shellcheck disable=SC2208
  if [ -v extensionsmap[$extension] ]
    then
      let extensionsmap[$extension]="${extensionsmap[$extension]} + $((1))"
    else
      extensionsmap[$extension]=1
    fi
}

# shellcheck disable=SC2120
# Функция для записи контрольной суммы и пути
post_sum() {
    local fullpath="$1"
    local checksum="$2"
    # shellcheck disable=SC2208
    if [ -v checksumap[$checksum] ]
    then
      checksumap[$checksum]="${checksumap[$checksum]},$fullpath"
    else
      checksumap[$checksum]="$fullpath"
    fi
}

# Функция для обработки файлов
process_file() {
    file="$1"
    size=$(stat -c %s "$file")
    checksum=$(md5sum "$file" | cut -d ' ' -f 1)
    # shellcheck disable=SC2155
    local fullpath=$(readlink -m $file)
    local ext=${file##*.}
    post_sum $fullpath $checksum
    post_extensions $ext
    echo -e "\033[33m File: $fullpath, Size: $size bytes, Checksum: $checksum, Extensions: $ext"
}

# Функция для обработки директорий
process_directory() {
    directory="$1"
    num_files=$(find "$directory" -type f | wc -l)
    total_size=$(du -csh "$directory" | tail -n 1 | cut -f 1)
    echo -e "\033[34m Directory: $directory, Number of Files: $num_files, Total Size: $total_size"
}

# Основная функция для обхода директории
explore_directory() {
    for entry in "$1"/*; do
        if [ -f "$entry" ]; then
            process_file "$entry"
            echo
        elif [ -d "$entry" ]; then
            process_directory "$entry"
            echo
            explore_directory "$entry"
        fi
    done
}

# Проверка наличия аргумента (пути к директории)
if [ -z "$1" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Запуск обхода директории
explore_directory "$1"
get_count_extensions
echo
get_checksum_double