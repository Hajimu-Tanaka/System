<?php

/*******************************************************
 ********** コードサンプル Todo
 *******************************************************/

/**
 * ルーティング  Todo
 */
Route::get('/folders/{id}/tasks', 'TaskController@index')->name('tasks.index');

/**
 * コントローラ  Todo
 */
namespace App\Http\Controllers;

use App\Folder;
use Illuminate\Http\Request;

class TaskController extends Controller
{
    public function index()
    {
        $folders = Folder::all();

        //テンプレートエンジンにデータを返す
        return view('tasks/index', [
            'folders' => $folders,
        ]);
    }
}


/* 以下はhasManyメソッドを使うことで省略できる */
$tasks = Tasks::where('folder_id', $current_folder->id)->get();
//⇩
$tasks = $current_folder->tasks()->get();

/**
 * マイグレーション  Todo
 */
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateFoldersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('folders', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->string('title', 20);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('folders');
    }
}

/**
 * モデル  Todo
 */
/*
 * 処理は全く書かなくても、Modelクラスを継承しているため、データ格納することができる。
 * テーブル名は複数形、モデル名は単数形で設定すること。
 */
namespace App;

use Illuminate\Database\Eloquent\Model;

class Folder extends Model
{
    //
}


/**
 * シーダー  Todo
 */
use Carbon\Carbon;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class FoldersTableSeeder extends Seeder
{
    public function run()
    {
        $titles = ['プライベート', '仕事', '旅行'];

        foreach ($titles as $title){
            DB::table('folders')->insert([
                'title' => $title,
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ]);
        }
    }
}





/**
 * ユニットテスト  Todo
 */


/*******************************************************
 ********** 設定ファイル Todo
 *******************************************************/

/**
 * .env Todo
 */
/*
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=taskdb
DB_USERNAME=test
DB_PASSWORD=test
 */

?>

<!-------------------------------------------------------
----------- Blade テンプレートエンジン Todo
-------------------------------------------------------->

<!--
    ここでは$foldersがコントローラから渡されたデータ
    {{ route() }} でルーティングで渡すリンクを作成できる
-->
<div class="list-group">
    @foreach($folders as $folder)
        <a href="{{ route('tasks.index', ['id' => $folder->id]) }}" class="list-group-item">
            {{ $folder->title }}
        </a>
    @endforeach
</div>