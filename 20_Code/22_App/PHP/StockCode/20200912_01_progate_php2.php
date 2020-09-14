<?php
/***************************************************
 *
 *  menu.php       ：Menuクラス
 *  data.php       ：データ定義
 *  index.php      ：トップページ
 *  confirm.php    ：注文内容確認ページ
 *
 ****************************************************/

/****************
 *　menu.php       ：Menuクラス Todo
 ****************/
class Menu {

    /**
     * 変数定義
     */
    private $name;
    private $price;
    private $image;
    private $orderCount = 0;

    /**
     * Menu constructor.
     * @param $name
     * @param $price
     * @param $image
     */
    public function __construct($name, $price, $image) {
        $this->name = $name;
        $this->price = $price;
        $this->image = $image;
    }

    public function hello() {
        echo '私は'.$this->name.'です';
    }

    public function getName() {
        return $this->name;
    }

    public function getImage() {
        return $this->image;
    }

    public function getOrderCount() {
        return $this->orderCount;
    }

    public function setOrderCount($orderCount) {
        $this->orderCount = $orderCount;
    }

    public function getTaxIncludedPrice() {
        return floor($this->price * 1.08);
    }

    public function getTotalPrice() {
        return $this->getTaxIncludedPrice() * $this->orderCount;
    }

}
?>

<?php
/****************
 *　data.php       ：データ定義 Todo
 ****************/
require_once('menu.php');

$juice = new Menu('JUICE', 600, 'https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/php/juice.png');
$coffee = new Menu('COFFEE', 500, 'https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/php/coffee.png');
$curry = new Menu('CURRY', 900, 'https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/php/curry.png');
$pasta = new Menu('PASTA', 1200, 'https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/php/pasta.png');

$menus = array($juice, $coffee, $curry, $pasta);

?>


<?php
/****************
 *　index.php      ：トップページ Todo
 ****************/

require_once('data.php')

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Café Progate</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <link href='https://fonts.googleapis.com/css?family=Pacifico|Lato' rel='stylesheet' type='text/css'>
</head>
<body>
<div class="menu-wrapper container">
    <h1 class="logo">Café Progate</h1>
    <form method="post" action="confirm.php">
        <div class="menu-items">
            <?php foreach ($menus as $menu): ?>
                <div class="menu-item">
                    <img src="<?php echo $menu->getImage() ?>" class="menu-item-image">
                    <h3 class="menu-item-name"><?php echo $menu->getName() ?></h3>
                    <p class="price">¥<?php echo $menu->getTaxIncludedPrice() ?>（税込）</p>
                    <input type="text" value="0" name="<?php echo $menu->getName() ?>">
                    <span>個</span>
                </div>
            <?php endforeach ?>
        </div>
        <input type="submit" value="注文する">
    </form>
</div>
</body>
</html>


<?php

/****************
 *　confirm.php    ：注文内容確認ページ Todo
 ****************/

require_once('data.php')
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Progate</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <link href='https://fonts.googleapis.com/css?family=Pacifico|Lato' rel='stylesheet' type='text/css'>
</head>
<body>
<div class="order-wrapper">
    <h2>注文内容確認</h2>

    <?php
        //合計金額を初期化
        $totalPayment=0
    ?>

    <?php foreach ($menus as $menu): ?>
        <?php
            $orderCount = $_POST[$menu->getName()];
            $menu->setOrderCount($orderCount);
            $totalPayment += $menu->getTotalPrice()
        ?>
        <p class="order-amount">
            <?php echo $menu->getName() ?>
            x
            <?php echo $orderCount ?>
            個
        </p>
        <p class="order-price"><?php echo $menu->getTotalPrice() ?>円</p>
    <?php endforeach ?>

    <h3>合計金額: <?php echo $totalPayment ?>円</h3>
</div>
</body>
</html>