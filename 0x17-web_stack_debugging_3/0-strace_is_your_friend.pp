#puppet script that does replace a file path

$file_path = '/var/www/html/wp-settings.php'

#replace "phpp" with "php"

exec { 'replace_line-errorr':

  command => "sed -i 's/phpp/php/g' ${file_path}",

  path    => ['/bin','/usr/bin']

}
