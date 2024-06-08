declare -A checksumap
declare -A extensionsmap

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

get_count_extensions(){
  echo "Double checksum:"
  for i in ${!extensionsmap[*]}
    do
    echo "$i = ${extensionsmap[$i]}"
    done
}

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

post_sum() {
    local fullpath="$1"
    local checksum="$2"
    echo "entry $fullpath, $checksum"
    # shellcheck disable=SC2208
    if [ -v checksumap[$checksum] ]
    then
      checksumap[$checksum]="${checksumap[$checksum]},$fullpath"
      echo "${checksumap[$checksum]}"
    else
      checksumap[$checksum]="$fullpath"
      echo "${checksumap[$checksum]}"
    fi
}

rand_ch() {
RANGE=10
number=$RANDOM
let "number %= $RANGE"
local  myresult=$number
echo "$myresult"
}

gen_folder() {
for (( c=1; c<=$(rand_ch); c++ ))
do
   echo "Welcome $c times"
done

}

a=$(rand_ch)

echo $a
gen_folder

#!/usr/bin/env bash

declare -A states
states=(
    [Germany]=112
    [Spain]=19
    [France]=21
    [Italy]=11
)

states[Russia]=$((states[Russia] + 1))

for i in ${!states[*]}
do
    echo "$i = ${states[$i]}"
done

# shellcheck disable=SC2208
if [ -v states[Germany] ]
then
    echo "Germany exists"
fi

#post_sum /home/lyapin/Documents/work_python/samples_and_tests/tests/radms/scan_stat.sh 05610e612e4e11ecd47252669561cde6
#post_sum /home/lyapin/Documents/work_python/samples_and_tests/tests/radms/scan_stat.sh 05610e612e4e11ecd47252669561cde6
post_extensions "sh"
post_extensions "sh"
post_extensions "txt"
get_count_extensions