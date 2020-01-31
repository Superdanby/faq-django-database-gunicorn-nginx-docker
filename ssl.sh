#!/bin/bash
if [[ -f /ssl/selfsigned.key && -f /ssl/selfsigned.crt && ${FORCE_NEW_CERT} != 'true' ]]; then
    cp /ssl/selfsigned.key /etc/ssl/private/selfsigned.key
    cp /ssl/selfsigned.crt /etc/ssl/certs/selfsigned.crt
else
    openssl req -x509 -nodes -days 7300 -newkey rsa:4096 -keyout /etc/ssl/private/selfsigned.key -subj "/C=${C}/ST=${ST}/L=${L}/O=${O}/OU=${OU}/CN=${CN}" -addext "subjectAltName = ${SAN}" -out /etc/ssl/certs/selfsigned.crt
    cp /etc/ssl/private/selfsigned.key /ssl/selfsigned.key
    cp /etc/ssl/certs/selfsigned.crt /ssl/selfsigned.crt
fi

if [[ -f /ssl/dhparam.pem && ${FORCE_NEW_CERT} != 'true' ]]; then
    cp /ssl/dhparam.pem /etc/nginx/dhparam.pem
else
    openssl dhparam -out /etc/nginx/dhparam.pem 4096
    cp /etc/nginx/dhparam.pem /ssl/dhparam.pem
fi

exec nginx -g 'daemon off;'
