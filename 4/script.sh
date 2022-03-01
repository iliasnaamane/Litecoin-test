docker rmi $(docker images -a  | grep hours | grep litecoin |  awk '3<$4 && $4<8' | awk '{print $3}')

