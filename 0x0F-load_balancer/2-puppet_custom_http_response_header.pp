# 2-puppet_custom_http_response_header.pp
# Puppet manifest to configure Nginx with custom X-Served-By header

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  require => Package['nginx'],
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
