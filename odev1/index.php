<?php

$saat = date("H");

if($saat >= 06 AND $saat <= 10){
    echo "Günaydın";
}

else if($saat >= 10 AND $saat <= 17){
    echo "İyi Günler";
}

else if($saat >= 17 AND $saat <= 20){
    echo "İyi akşamlar";
}

else if($saat >=20 AND $saat <=00){
    echo "iyi Geceler";
}

else{
    echo "Esenlikler Dilerim";
}


?>