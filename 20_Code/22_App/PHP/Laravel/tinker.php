#テストデータの確認
php artisan tinker

<?php

/****************************************
 * テストデータ確認
 ****************************************/
//現在アクセスしているユーザーがSessionが有効状態か確認
Auth::check();

//フォルダテーブルから ID カラム（プライマリキー）が 1 である行のデータを検索
\App\User::find(1);
\App\Folder::find(1);

//'folder_id'カラムで、前行の$folder->idに対応する情報を取得する
\App\Task::where('folder_id', $folder->id)->get();
\App\Task::where('folder_id', 1)->get();

//SQL文を取得する
\App\Task::where('folder_id', 1)->toSql();
\App\Folder::find(1)->toSql();

//モデルに対応するテーブルデータを全て取得
use App\Folder;
$folders = Folder::all(); //


/**
 * Carbon
 *
 * DateTimeクラスをオーバーラップした日付操作ライブラリ
 * https://qiita.com/yudsuzuk/items/ff894bd0b76d4657741d
 */

use Carbon\Carbon;
Carbon::now();
Carbon::today();
Carbon::tomorrow();
Carbon::yesterday();
Carbon::parse('2016-04-30 10:32:32');
Carbon::now()->year;
