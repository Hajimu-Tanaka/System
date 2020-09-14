<!--
    /Users/tanakahajimu/workspace/utilities/Sub/HTML_CSS/sample.html
-->
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>

<body>

    <!-------------------------->
    <!--  ヘッダー部   -->
    <!-------------------------->
    <header>

    </header>

    <!-------------------------->
    <!--  メイン部   -->
    <!-------------------------->
    <main>

        <div class="top-wrapper">
            <!--  -->
            <div class="container">
                <h1>LEARN TO CODE.</h1>
                <h1>LEARN TO BE CREATIVE.</h1>
                <p>Progateはオンラインプログラミング学習サービスです。</p>
                <p>初心者にもやさしいスライドとレッスンで、Webサービスを作りながらプログラミングを学んでいきましょう。</p>
                <!-- ボタンラッパー -->
                <div class="btn-wrapper">
                    <a class="btn signup" href="#">新規登録はこちら</a>
                    <p>or sign up with</p>
                    <a class="btn facebook" href="#">Facebookで登録</a>
                    <a class="btn twitter" href="#">Twitterで登録</a>
                </div>
            </div>
        </div>

        <div class="second-wrapper">
        </div>



        <div class="third-wrapper">

            <!-- -------------------------------- -->
            <!-- フォーム部 ----------------------- -->
            <!-- -------- ----------------------- -->
            <form method="post" action="sent.php">

                <input type="text" name="" value="" />
                <input type="hidden" name="" value="" />
                <input type="button" name="" value="" />
                <input type="image" name="" value="" />
                <textarea name="" id= rows="8" cols="40"></textarea>

                <select name="age">
                    <option value="未選択">選択してください</option>
                    <option value="20代">20代</option>
                    <option value="30代">30代</option>
                </select>

                <input type="submit" name="" value="送信" />
            </form>

        </div>

    </main>

    <!-------------------------->
    <!--  フッター部   -->
    <!-------------------------->
    <footer>

    </footer>

</body>

</html>



<?php


?>

<div class="main">
    <div class="thanks-message">お問い合わせいただきありがとうございます。</div>
    <div class="display-contact">

        <div class="form-title">入力内容</div>

        <div class="form-item">■ 名前</div>
        <?php echo $_POST['name']; ?>

        <div class="form-item">■ 年齢</div>
        <?php echo $_POST['age']; ?>

        <div class="form-item">■ 内容</div>
        <?php echo $_POST['body']; ?>

    </div>
</div>


