
/**************************************************************
 *******SQL文の分類 Todo
 **************************************************************/

--DML（データ操作言語）
SELECT:データの取り出し
INSERT:新規データの挿入
UPDATE:既存データの更新
DELETE:既存データの削除
MERGE:データのマージ

--DDL（データ定義言語）
CREATE:オブジェクトの作成
ALTER:オブジェクト定義の変更
DROP:オブジェクトの削除
RENAME:オブジェクト名の変更
TRUNCATE:表の切り捨て
COMMENT:コメントの定義

--DCL（データ制御言語）
GRANT:権限の付与
REVOKE:権限の取り消し

--トランザクション制御
COMMIT:変更の確定
ROLLBACK:変更の取り消し
SAVEPOINT:セーブポイントの作成


/**************************************************************
 *******SELECT文を用いたデータの取得 Todo
 **************************************************************/

/* 表構造の表示 */
DESCRIBE emp;
DESC emp;


/* 算術演算子の使用 */

/* 列別名の使用 */

/* 連結演算子の使用 */

/* 重複行の排除 */
SELECT DISTINCT job FROM emp;                         --重複行を排除し、一意で表示
SELECT DISTINCT deptno, job FROM emp;                 --複数列組み合わせでの重複行も可能
-- SELECT DISTINCT deptno, DISTINCT job FROM emp;     --エラー
-- SELECT deptno, DISTINCT job FROM emp;              --エラー


/**************************************************************
 *******データの制限およびソート　Todo
 **************************************************************/

/* 比較演算子 */
SELECT ename FROM emp WHERE deptno = 10;                  --等しい
SELECT empno FROM emp WHERE deptno > 10;                  --大きい
SELECT empno FROM emp WHERE deptno >= 10;                 --以上
SELECT empno FROM emp WHERE deptno < 10;                  --小さい
SELECT empno FROM emp WHERE deptno <= 10;                 --以下
SELECT empno FROM emp WHERE deptno <> 10;                 --等しくない
SELECT empno FROM emp WHERE deptno != 10;                 --等しくない
SELECT empno FROM emp WHERE deptno ^= 10;                 --等しくない
SELECT empno FROM emp WHERE deptno BETWEEN 10 AND 20;     --10以上20以下
SELECT empno FROM emp WHERE deptno NOT BETWEEN 10 AND 20; --10以上20以下以外
SELECT empno FROM emp WHERE deptno IN(10,20,30,40);       --いずれか
SELECT empno FROM emp WHERE deptno NOT IN(10,20,30,40);   --いずれか以外
SELECT empno FROM emp WHERE ename LIKE '%中太%';           --文字パターン一致
SELECT empno FROM emp WHERE ename NOT LIKE '%中太%';       --文字パターン一致しない
SELECT empno FROM emp WHERE deptno is NULL ;              --値がNULL
SELECT empno FROM emp WHERE deptno is NOT NULL ;          --値がNULL以外

/* ワイルドカード */
SELECT empno FROM emp WHERE ename LIKE '%中太%';          -- %は０文字以上の任意の文字列と一致
SELECT empno FROM emp WHERE ename LIKE '_中太_';          -- 任意の１文字と一致する
SELECT empno FROM emp WHERE ename LIKE '____';           -- enameが４文字のデータを取得
SELECT empno FROM emp WHERE ename LIKE '%____消しゴム';
    --末尾に「消しゴム」が付き、８文字以上
SELECT empno FROM emp WHERE ename LIKE '100¥%%' ESCAPE '¥';
    --「¥」をエスケープ文字とし、先頭に「100％」を含む文字列を取得

/* 論理演算子 */
SELECT empno FROM emp WHERE deptno = 10 AND sal = 200000;
SELECT empno FROM emp WHERE deptno = 10 OR sal = 200000;
    --AND、ORの優先順位で比較される。カッコ（）を使えば変更できる
SELECT empno FROM emp WHERE NOT sal = 200000;
    --NOT演算子は、条件がFALSEの場合にTRUEを返す

/* ソート */
SELECT empno FROM emp ORDER BY sal;                     --昇順
SELECT empno FROM emp ORDER BY sal DESC;                --降順
SELECT empno FROM emp WHERE deptno = 10 ORDER BY sal;   --where句との併用
SELECT empno FROM emp ORDER BY sal DESC, deptno;
    --salで降順にソートし、続いてdeptnoの列で昇順にソート

--ソート順序はデータ型により異なる
--数値:小さい値から大きい数値
--日付値:古い日付から新しい日付
--文字値:アルファベット、続いて５０音順（文字コード順）
--NULL：最も大きい値として扱われる



/**************************************************************
 *******SQL関数　単一行関数　Todo
 **************************************************************/

 /**　基礎知識　*/

--１件の入力データ毎に処理を行い、入力データ毎に結果を１つ返す関数




/**
 大文字・小文字変換関数
 */

/* UPPER関数 ：すべて大文字に変換　*/
SELECT ename, UPPER(ename) FROM emp;                --すべて大文字に変換
SELECT ename FROM emp UPPER(ename) = 'TANAKA';      --比較の際も利用可能

/* LOWER関数 ：すべて小文字に変換 */


/* INITCAP関数 ：最初の文字だけ大文字に変換 */


/**
 文字操作関数 　Todo
 */

/* CONCAT関数 ：２つの文字列連結 */
SELECT CONCAT('Oracle','Server') FROM DUAL;

/* SUBSTR関数 ：文字列のm番目の文字からn文字分の文字列を返す（抜き出す） */
SELECT SUBSTR('Oracle Server',2 ,3) FROM DUAL;      -- 結果：rac
SELECT SUBSTR('Oracle Server',2) FROM DUAL;         -- 結果：racle Server
SELECT SUBSTR('Oracle Server',-6,3) FROM DUAL;      -- 結果：Ser (後から６文字で、３文字分)
SELECT SUBSTR('Oracle Server',-6) FROM DUAL;        -- 結果：Server（後から６文字、それ以降）

/* LENGTH関数 ：文字数を返す */
SELECT LENGTH('Oracle Server') FROM DUAL;              -- 結果：13

/* INSTR関数 ：「指定した文字パターンが現れる位置」を返す */
SELECT INSTR ('Oracle Server','er') FROM DUAL;        -- 結果：12
SELECT INSTR ('Oracle Server','er',1 ,2) FROM DUAL;   -- 結果：9

/* LPAD関数 ： 文字列の左側に、引数として受け入れた文字列がn文字になるように「埋め込み文字」挿入 */
SELECT LPAD (yomi,10,'*') FROM emp; -- 結果：******sato

/* RPAD関数 ： 文字列の右側に、引数として受け入れた文字列がn文字になるように「埋め込み文字」挿入 */
SELECT RPAD (yomi,10,'*') FROM emp; -- 結果：sato******

/* TRIM関数 ：前後にあう「削除文字」（任意の１文字）を取り除く */
SELECT TRIM (LEADING 'O' FROM 'Oracle Server') FROM DUAL;  -- 結果：racle Server
SELECT TRIM (TRAILING 'r' FROM 'Oracle Server') FROM DUAL; -- 結果：Oracle Serve
SELECT TRIM ('    Oracle Server   ') FROM DUAL;            -- 結果：Oracle Server
    --デフォルトでは、両端の半角スペース削除
SELECT LENGTH(TRIM ('    Oracle Server   ')) FROM DUAL;    -- 結果：13

/* REPLACE関数 ：変更前文字列を変更後文字列に置き換えた文字列を返す */
SELECT LENGTH('Oracle Server','Server','Master') FROM DUAL;
    --結果：Oracle Master
SELECT LENGTH('Oracle Server','Server') FROM DUAL;
    --結果：Oracle   変更後文字列省略すると、削除される


/**
 数値関数 　Todo
 */

/* ROUND関数 ：小数点以下n桁に四捨五入して返す */


/* TRUNC関数 ： */


/* MOD関数 ： */


/**
 日付関数 　Todo
 */

/* 日付値の基礎知識 */

/* SYSDATE関数*/

/* MONTH_BETWEEN関数 */

/* ADD_MONTHS関数 */

/* NEXT_DAY関数 */

/* LAST_DAY関数 */

/* ROUND関数(日付) */

/* TRUNC関数(日付) */

/**************************************************************
 *******暗黙的なデータ方変換　Todo
 **************************************************************/


/**************************************************************
 *******明示的なデータ型変換と主な変換関数　Todo
 **************************************************************/

/* TO_CHAR関数(日付→文字値) */

/* TO_CHAR関数(数値→文字値) */

/* TO_DATE関数 */

/* TO_NUMBER関数 */


/**************************************************************
 *******汎用関数　Todo
 **************************************************************/

/* NVL関数 */

/* NVL2関数 */

/* NULLIF関数 */

/* COALESCE関数 */

/* CASE式 */

/* DECODE関数 */


/**************************************************************
 *******SQL関数　グループ関数　Todo
 **************************************************************/

 /**　基礎知識　*/
--複数件の入力データをグループ化して、集計処理を行った結果を１つだけ戻す関数
--グループ関数は、SELECT句、ORDER BY句、HAVING句で利用できる
--グループ関数ではWHERE句は利用できない
--DISTINCTを指定すると、重複した値は１回だけ処理される

/* COUNT関数 */

/* MAX関数 */

/* MIN関数 */

/* AVG関数 */

/* SUM関数 */

/* グループ関数のいろいろな使い方 */


/**************************************************************
 ******* 複数のテーブルからのデータ取り出し　Todo
 **************************************************************/



/**************************************************************
 ******* 副問合せ　Todo
 **************************************************************/

/* 単一行副問合せ */

/* 複数行副問合せ */


/**************************************************************
 ******* 集合演算子　Todo
 **************************************************************/

/* UNION演算子 */

/* UNION ALL演算子 */

/* INTERSECT演算子 */

/* MINUS演算子 */

/* 集合演算子 ガイドライン */



/**************************************************************
 *******データ操作 Todo
 **************************************************************/

/* INSERT文によるデータ追加 */

/* UPDATE文によるデータ更新 */

/* DELETE文によるデータ削除 */


/**************************************************************
 *******明示的なトランザクション制御 Todo
 **************************************************************/



/**************************************************************
 *******暗黙的なトランザクション制御 Todo
 **************************************************************/

/* 自動コミット */

--DDL文の実行時
--DCL文の実行時
--SQL Development または SQLPlusの正常終了時

/* 自動ロールバック */

--SQL Development または SQLPlusの異常終了時
--システム障害発生時（Oracleインスタンスの異常停止時）

/* TRUNCATE文 */

--TRUNCATE文では、削除するデータを指定できない
--TRUNCATE文はDDL文なので、実行時に自動コミットが実行される
--自動コミットが実行されるので、処理をロールバックできない
--TRUNCATE文ではロールバック用のデータを生成する必要がないため、短時間でデータを削除できる



/**************************************************************
 *******同時実行制御 Todo
 **************************************************************/

/* 読み取り一貫性 */

/* ロック */

/* FOR UPDATE句による排他ロック */




/**************************************************************
 *******DDL文を使用した表の作成と管理 Todo
 **************************************************************/



/**************************************************************
 *******Oracle ちょこっとリファレンス Todo
 **************************************************************/


/*****************************
 DATABASE（データベース）
 *****************************/

/*
 DATABASEはオラクルの最も基本的な部分
 オラクルデータベースは、DATABASEを作成してその中にTABLESPACEという領域を作成して、
 さらにその中にTABLEとかINDEXなどを作成する作りとなっている。

 https://oracle-chokotto.com/ora_database.html

 DATABASEの作成には、CREATE DATABASE句を使用
 SYSDBA権限でアイドルインスタンスに接続したうえで、CREATE DATABASE文をオラクルをNOMOUNT状態で実行

 */


--CONN SYS/change_on_install AS SYSDBA　（パスワードはデフォルトの場合）
--STARTUP NOMOUNT SPFILE=C:\init.ora　（ファイルは、C:\init.ora）

--例：TESTDBというデータベースを作成する
CREATE DATABASE TESTDB
  LOGFILE GROUP 1 ('C:\DATAFILE\REDO\REDO01A.log',           -- REDOログファイルの作成場所、サイズ、グループとメンバーの構成を指定
                   'C:\DATAFILE\REDO\REDO01B.log') SIZE 10M
          GROUP 2 ('C:\DATAFILE\REDO\REDO02A.log',
                   'C:\DATAFILE\REDO\REDO02B.log') SIZE 10M
  DATAFILE 'C:\DATAFILE\DATA\SYSTEM01.dbf' SIZE 256M         --	SYSTEM表領域ファイルの作成場所、サイズを指定
  AUTOEXTEND ON NEXT 64M                                     -- 表領域ファイルの自動拡張の指定
  MAXSIZE UNLIMITED
  SYSAUX DATAFILE 'C:\DATAFILE\DATA\SYSAUX01.dbf' SIZE 256M
  DEFAULT TEMPORARY TABLESPACE TEMP01
    TEMPFILE 'C:\DATAFILE\DATA\TEMP01.dbf' SIZE 256M
  UNDO TABLESPACE UNDO01
    DATAFILE 'C:\DATAFILE\DATA\UNDO01.dbf' SIZE 256M
  ARCHIVELOG
  CHARACTER SET JA16SJISTILDE
;


/*****************************
 TABLESPACE（表領域）
 *****************************/

/*
    表領域とはオブジェクト（表・ビュー・索引など）を格納するひとまとまりの領域
    表領域は物理的なファイルと対応しており、「１表領域＝１つ以上のデータファイル」となっている。
    しかし、１データファイルが複数の表領域を格納することはない。

 */

/* 表領域の作成 */
--（例）表領域(USER01)をファイル名「USER01.dbf」、100MBのサイズで作成する
CREATE TABLESPACE USER01
  DATAFILE 'D:\ORACLE\DATA\USER01.dbf' SIZE 100M
  SEGMENT SPACE MANAGEMENT AUTO
;

/* 表領域の書き込み可/不可の変更 */
--（例）表領域（表領域名：test_tbs）を書き込み不可にする。
ALTER TABLESPACE test_tbs READ ONLY;

つづく


/*****************************
 TABLE（表）
 *****************************/

/*

    https://oracle-chokotto.com/ora_table.html
 */


/* 表の作成 */

/* 列の追加・削除・変更 */
ALTER TABLE test_tab ADD (column2 VARCHAR2(20));        --（例）列（列名：column2/型：VARCHAR2(20)）をtest_tab表に追加する。
ALTER TABLE test_tab MODIFY tel VARCHAR2(15) NOT NULL;  --（例）列（列名：tel/型：VARCHAR2(15)）の制約にNOT NULLを設定する。
ALTER TABLE test_tab DROP COLUMN tel;                   --（例）列（列名：tel/型：VARCHAR2(15)）をtest_tab表から削除する。

/* 表名の変更 */
RENAME test_tab TO my_tab;                              --（例）表(test_tab)を、my_tabに名称変更する。

/* 表の削除 */
DROP TABLE test_tab CASCADE CONSTRAINTS;                --（例）表（表名：test_tab）を削除する。

/* テーブルの情報を表示する */
SELECT * FROM ALL_TABLES;



 /*****************************
 VIEW（ビュー）
 *****************************/

 /*
    ビューとはある表の特定のカラムや指定した条件に合致するレコードなどを取り出した仮想の表
    また複数の表を結合したビューを作成することもできる。

    ビューを作成することによりユーザに必要最小限のカラムやレコードのみにアクセスさせる事ができたり、
    結合条件を指定しなくても既に結合された表にアクセスできるなどのメリットがあります。

    https://oracle-chokotto.com/ora_view.html
  */



 /*****************************
 INDEX（インデックス/索引）
 *****************************/
https://oracle-chokotto.com/ora_index.html

 /*****************************
 SEQUENCE（シーケンス/順序）
 *****************************/
https://oracle-chokotto.com/ora_sequence.html


 /*****************************
 TRIGGER（トリガー）
 *****************************/
https://oracle-chokotto.com/ora_trigger.html


 /*****************************
 SYNONYM（シノニム/別名）
 *****************************/
https://oracle-chokotto.com/ora_synonym.html


 /*****************************
 USER（ユーザー）
 *****************************/
https://oracle-chokotto.com/ora_user.html


 /*****************************
 ROLE（ロール）
 *****************************/
https://oracle-chokotto.com/ora_role_c.html


 /*****************************
 PROFILE（プロファイル）
 *****************************/
https://oracle-chokotto.com/ora_profile.html


 /*****************************
 FUNCTION（ファンクション/関数）
 *****************************/
https://oracle-chokotto.com/ora_databaselink.html



 /*****************************
 PROCEDURE（プロシージャ）
 *****************************/
https://oracle-chokotto.com/ora_procedure.html



 /*****************************
 PACKAGE（パッケージ）
 *****************************/
https://oracle-chokotto.com/ora_package.html



 /*****************************
 DIRECTORY（ディレクトリ）
 *****************************/
https://oracle-chokotto.com/ora_directory.html


 /*****************************
 初期化パラメータ
 *****************************/
https://oracle-chokotto.com/ora_initparam.html

/*
    初期化パラメータではデータベース全体に関わる設定を行う

 */

SHOW PARAMETERS             --初期化パラメータの一覧と値を確認する


 /*****************************
 システム変数
 *****************************/
https://oracle-chokotto.com/ora_sysparam.html

/*
    システム変数でSQL*Plusでの表示方法や動作を設定できる
 */


 /*****************************
 データディクショナリビュー
 *****************************/

/*
    データディクショナリビューとは
    データベース内のオブジェクト（表やビュー、索引、プロシージャなどなど）や
    表領域、ユーザ、権限などデータベースに係わる様々な情報をテーブル形式で取得することができるもの

    https://oracle-chokotto.com/ora_ddv.html

    データディクショナリには大きく分けて、以下がある
    ・「DBA_」で始まるもの       ：   データベース内全てのオブジェクトに関する情報
    ・「ALL_」で始まるもの       ：   自分がアクセスできるオブジェクトに関する情報
    ・「USER_」で始まるもの      ：   自分の所有するオブジェクト（自スキーマのオブジェクト）に関する情報
    ・その他                   ：   セッションやロール、言語環境に関する情報

    ※作成されていない場合は、以下で作る必要があるらしい。
    ORACLE_HOME=/opt/oracle/product/12.2.0.1/dbhome_1
    /opt/oracle/product/12.2.0.1/dbhome_1/rdbms/admin/catalog.sql

 */

SELECT TABLE_NAME FROM DICTIONARY;      --データディクショナリの一覧を表示する（全表示時間かかるので要注意）

/* 主要データディクショナリ */
SELECT * FROM USERS;                    --


 /*****************************
 V$表（動的パフォーマンスビュー）
 *****************************/

/*
    V$表はOracleサーバの現在のさまざまな状態を調べたいときに使用
    名前に「動的」と付くように取得できる値は刻々と変わる。

    https://oracle-chokotto.com/ora_vtable.html
*/

/* V$表の一覧を取得する（要権限） */
SELECT OBJECT_NAME FROM DBA_OBJECTS WHERE OBJECT_NAME LIKE 'V$%';


SELECT * FROM V$BACKUP;         --データファイルがオンラインバックアップ中かどうか調べる
SELECT * FROM V$CONTROLFILE;    --制御ファイルに関する情報を調べる
SELECT * FROM V$INSTANCE;       --接続中のインスタンス名やバージョンを調べる
SELECT * FROM V$DATABASE;       --接続中のデータベース名や作成日を調べる


 /*****************************
 ロール
 *****************************/

/*
    ロールとは、複数の権限をまとめて一つにしたもの
    権限をユーザに付与する場合は、権限を直接ユーザに付与せずに、
    一旦ロールに権限を持たせてからそのロールをユーザへ付与する方法が一般的。
    これにより権限の管理が非常に簡単になり、間違いも少なくなる。

    https://oracle-chokotto.com/ora_role.html

*/


 /*****************************
 権限
 *****************************/


/*
    権限とはデータベースにログインしたユーザに許可する操作の事
    例えば、更新や削除は行って欲しくないというユーザには、検索の権限のみ与えるというような使い方をする。

    Oracleの権限には「オブジェクト権限」と「システム権限」がある。
    https://oracle-chokotto.com/ora_auth.html

*/



/*****************************
 recyclebin（リサイクルビン）
 *****************************/

/*
    recyclebin（リサイクルビン）とはOracle10gより導入された新機能で、Windowsでいう「ゴミ箱」と同じ考え方のもの
    表をDROPしても完全には削除されないため、ゴミ箱（リサイクルビン）から簡単に復活させることができるようになる。

    https://oracle-chokotto.com/ora_recyclebin.html
 */


--リサイクルビン（ゴミ箱）の中身を確認する
show recyclebin;

--リサイクルビン（ゴミ箱）から表を復活させる
flashback table "BIN$ELBSLJRLcG/len88e3Nw==$0" to before drop;

--リサイクルビンのクリア
PURGE RECYCLEBIN;




/**************************************************************
 *******Tips Todo
 **************************************************************/

/* DUAL：データが１件だけ入っていることを保証する表 */
SELECT * FROM DUAL;

