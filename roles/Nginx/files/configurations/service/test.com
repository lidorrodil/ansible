server {
    listen 80;
    listen [::]:80;

    root /var/www/test.com/html;
    index index.html index.htm;

    server_name test.com www.test.com;

    error_page 404 401 403 /custom_404.html;
    location = /custom_404.html {
            root /usr/share/nginx/html;
            internal;
    }

    error_page 500 502 503 504 /custom_50x.html;
    location = /custom_50x.html {
            root /usr/share/nginx/html;
            internal;
    }


    location / {
#	proxy_pass www.google.com;
        try_files $uri $uri/ =404;
        auth_basic "Restricted Content";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
}
