<?php

$files = glob(dirname(__FILE__) . '/*.xls');
$file = end($files);
$url = 'https://tienrocker.com/api/upload_process';

$postData = array(
    'name' => basename($file),
    'data' => base64_encode(file_get_contents($file))
);

$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => 1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $postData,
));

$response = curl_exec($curl);

$info = curl_getinfo($curl);
//echo "code: ${info['http_code']}";

//print_r($info['request_header']);

var_dump($response);
$err = curl_error($curl);

echo "error";
var_dump($err);
curl_close($curl);
