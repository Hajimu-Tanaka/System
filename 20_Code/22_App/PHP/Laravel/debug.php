<?php

/**
 * LARAVEL/PHPでよく使うデバッグ方法
 * https://qiita.com/a05kk/items/e05a1508dc562861fcf5
 */

// debug()
$array = array(1,2,3,'いち','に','さん');
dump($array);


// var_dump();
$array = array(1,2,3,'いち','に','さん');
var_dump($array);


//dd();
$array = array(1,2,3,'いち','に','さん');
dd($array);

/**
 * Debugbar
 */
public function store(Request $request)
{
    $like = new Like;
    \Debugbar::info(1);
    $like->user_id = $request->user;
    \Debugbar::info(2);
    $like->post_id = $request->post;
    \Debugbar::info(3);
    \Debugbar::info($like);
    $like->save();

    return;
}