function proxy_off(){
    unset http_proxy
    unset https_proxy
    echo -e "Proxy dislabled"
}
function proxy_on() {
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
    export http_proxy="http://127.0.0.1:8118"
    export https_proxy=$http_proxy
    echo -e "Proxy enabled"
}

alias db="python3 ~/lalamove/tools/connect_db.py"
alias server="~/web/connect/all.sh"
