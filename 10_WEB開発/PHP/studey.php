<?php

/*******************************************************
 * 基本構文 Todo
 *******************************************************/

//標準出力
echo "Hello world!";
echo 7 * 2;
echo 8 % 3;
echo '5 + 7';

//変数
$fruit = 'りんご';
echo $fruit;

//文字連結
$name = 'tanakaです';
echo 'こんにちは！' . $name;

/**
 * 判定文
 */
$x = 1071;
if($x % 3 == 0 && $x % 7 == 0 ){
    echo 'xは3の倍数かつ7の倍数です。';
}elseif($x % 3 == 0 && $x % 7 != 0){
    echo 'xは3の倍数ですが7の倍数ではありません。';
}elseif($x % 3 != 0 && $x % 7 == 0){
    echo 'xは7の倍数ですが3の倍数ではありません。';
}else{
    echo 'xは7の倍数でも3の倍数でもありません。';
}

/**
 * Switch文
 */
$remainder = 0;
switch ($remainder){
    case 0:
        echo '大吉です。';
        break;
    case 1:
        echo '中吉です。';
        break;
    case 2:
        echo '小吉です。';
        break;
    default:
        echo '凶です。';
        break;
}

/**
 * 配列
 */

//配列
$colors = array('赤','青','黄');
echo $colors[0];
$colors[3] = '白';               //要素追加
echo $colors[3];

//連想配列
$scores = array(
    '数学' => 70,
    '英語' => 90,
    '国語' => 80,
);
$scores['国語'] += 5;
echo $scores['国語'];

/**
 * for文
 */
//501以上でbreak
for($i=1; $i<=1000; $i++){
    if($i >= 501){
        break;
    }
    echo $i;
    echo '<br>';
}

//３の倍数はcontinue
for($i=1; $i<=1000; $i++){
    if($i % 3 == 0){
        continue;
    }
    echo $i;
    echo '<br>';
}

/**
 * While文
 */
while($i <= 100){
    echo $i;
    echo '<br>';
    $i += 2;
}

/**
 * foreach文
 */
//配列または連想配列に対して、先頭のデータから順に繰り返し処理を行うための命令
$scores = array('数学' => 70, '英語' => 90, '国語' => 80);
foreach($scores as $key => $value){
    echo $key . 'は' . $value . '点です。';
}

?>

<!---------------------------------------------------------------------->

<?php
/*******************************************************
 * 関数 Todo
 *******************************************************/

/**
 * 標準関数
 */
$str = 'sample';
echo strlen($str);          //文字数

$array = array('HTML', 'CSS', 'PHP');
echo count($array);         //$arrayの要素数

echo rand(10,15);           //ランダムな数字を返す（例：１０〜１５）
echo floor(12.16);    //小数点以下切り捨て


/**
 * 関数の定義
 */
//返り値なし
function printRectangleArea($height,$width){
    echo $height * $width;
}
printRectangleArea(5,10);

//返り値あり
function getCircleArea($radius){
    return $radius * $radius * 3;
}
$circleArea = getCircleArea(5);
echo $circleArea;

?>

<!---------------------------------------------------------------------->
<?php
/*******************************************************
* HTML Todo
*******************************************************/
?>

<?php
/*******************************
 * Selectタグ
 *******************************/
?>

<!-- 送信元 -->
<select name="age">
    <option value="未選択">選択してください</option>
    <!-- for文を用いて6歳から100歳までをoptionで選べる -->
    <?php
        for($i=6;$i<=100;$i++){
            echo '<option value="' . $i . '">' . $i . '</option>';
        }
    ?>
</select>

<select name="category">
    <option value="未選択">選択してください</option>
    <?php
        $types = array('仕事','その他');
        foreach($types as $type){
            echo '<option value="' . $type . '">' . $type . '</option>';
        }
    ?>
</select>

<!-- 送信先 -->
<div class="form-item">■ 年齢</div>
<?php echo $_POST['age']; ?>

<div class="form-item">■ お問い合わせの種類</div>
<!-- この下でcategoryを受け取りechoしましょう -->
<?php echo $_POST['category']; ?>


<?php
/*******************************************************
* クラス Todo
*******************************************************/
?>

<?php
/**
 * クラス
 * menu.php
 */
class Menu {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function hello() {
        echo '私は'.$this->name.'です';
    }
}
?>

<?php
/**
 * データ
 * data.php
 */
require_once('menu.php');

$juice = new Menu('JUICE');
$coffee = new Menu('COFFEE');
$curry = new Menu('CURRY');
$pasta = new Menu('PASTA');
$menus = array($juice, $coffee, $curry, $pasta);

?>

<?php
/**
 * データ
 * index.php
 */


?>

