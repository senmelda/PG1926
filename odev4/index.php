<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<title>Ödev 4 </title>
        <link rel="stylesheet" href="index.css">
	</head>
	<body>
    <?php
        
        
        if(isset($_POST))
        {
        echo "<h1>Para Üstü : ".$_POST["paraustu"]."</h1>";
        
        $birlik = $paraustu/1;
        if($birlik > 0){
           $paraustu%=1;
           echo $birlik + 'adet 1 TL';
        }
        $ellikurus = $paraustu/0.5;
        if($ellikurus > 0){
           $paraustu%=0.5;
           echo $ellikurus + 'adet 50 krş';
        }
        $ybeskurus = $paraustu/0.25;
        if($ybeskurus > 0){
           $paraustu%=0.25;
           echo $ybeskurus + 'adet 25 krş';
        }
        $onkurus = $paraustu/0.10;
        if($onkurus > 0){
           $paraustu%=0.10;
           echo $onkurus + 'adet 10 krş';
        }
        $beskurus = $paraustu/0.05;
        if($beskurus > 0){
           $paraustu%=0.05;
           echo $beskurus + 'adet 5 krş';
        }
        $birkurus = $paraustu/0.01;
        if($birkurus > 0){
           $paraustu%=0.01;
           echo $birkurus + 'adet 1 krş';
        }
    }
    else{
        echo "Para üstü girişi yapılmadı";
    }
                
        
?>
        <form action="" method="post">
            <input type="text" name="paraustu">
            <input type="submit" name="gonder" value="Hesapla">
        </form>
	</body>
</html>


