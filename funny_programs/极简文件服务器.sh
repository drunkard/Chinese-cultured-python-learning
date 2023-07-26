[ $1 ] && [ -d $1 ] && python3 -m http.server 9090 || echo "用法: $0 <要分享的目录>"
