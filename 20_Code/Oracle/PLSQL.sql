
/***************************************************
 PL/SQLの基礎 Todo
 ***************************************************/

/**
  基本
 */
--変数宣言部
DECLARE
    str VARCHAR2(30);
--処理部
BEGIN
    str := 'HELLO WORLD';           -- 変数へ代入
    DBMS_OUTPUT.PUT_LINE(str);      -- コンソール出力
END;

/**
  IF文
 */
DECLARE
    name VARCHAR2(10);
    message VARCHAR2(10);
BEGIN
    name := 'tanaka';

    if(name = 'tanaka') then
        message := '名前はtanakaです。';
    elsif(name = 'yamada') then
        message := '名前はyamadaです。';
    else
        message := '名前はありません';
    end if;

    DBMS_OUTPUT.PUT_LINE(message);
END;

/**
  FOR文
 */
DECLARE

BEGIN
    for i in 1..12 loop
        if (i in 2,4,6,9,11) then
            DBMS_OUTPUT.PUT_LINE(i || '月は「小の月」です'); -- 文字列連結
        else
            DBMS_OUTPUT.PUT_LINE(i || '月は「小の月」です');
        end if;
    end loop;
END;


/**
  例外処理
 */

--宣言部
DECLARE
    name VARCHAR2(10);
    noNameException EXCEPTION ;
--処理部
BEGIN
    name := '';

    IF (name is not null) THEN
        DBMS_OUTPUT.PUT_LINE('名前は' || name || 'です。');
    ELSE
        RAISE noNameException;
    END IF;

--例外処理部
EXCEPTION
    WHEN noNameException THEN
        DBMS_OUTPUT.PUT_LINE('名前がありません。');
END;



/***************************************************
 ストアドプロシージャ Todo
  https://www.shift-the-oracle.com/plsql/user-function-procedure.html
 ***************************************************/

--ストアド・プロシージャはクライアントとサーバーを繋ぐネットワークという遅い通信経路に
--SQLと結果が何度も行き交うような処理に対して非常に有効

/**
  基本
 */

-- ファンクション名の宣言
CREATE OR REPLACE FUNCTION RIVUS.PRODUCT --上書き防止のためプログラムは RIVUS ユーザーで定義されている
(
    --パラメータの定義
    P_NUM1 IN NUMBER,   -- P_NUM1 : 数値(IN パラメータ:入力のみ)
    P_NUM2 IN NUMBER    -- P_NUM2 : 数値(IN パラメータ:入力のみ)
)
    --戻り値の定義 ( RETURN 句 )
    RETURN NUMBER       -- 戻り値 P_NUM1 × P_NUM2 : 数値
    IS
    vSum	NUMBER(2) DEFAULT  0;
        --入力数値は四捨五入により整数に丸められた数値で計算される。
        --正の数値の掛け算で、かつ、結果が 100 未満であること。

--処理部
BEGIN
    FOR i IN 1..P_NUM2
        LOOP
            vSum := vSum + P_NUM1;
        END LOOP;

    --戻り値
    RETURN vSum ;
END;
/

SELECT PRODUCT(5,6) FROM DUAL ;     -- 結果：30
SELECT PRODUCT(5,-1) FROM DUAL ;    -- 結果：0


/***************************************************
 Oracleのジョブでスケジュール実行 Todo
  https://sql-oracle.com/?p=164
 ***************************************************/


/**
  ジョブの基礎知識
 */

--夜間のバッチ処理や定期的な処理はジョブでスケジュール実行すると便利
--ジョブはOracleの「DBMS_SCHEDULER」パッケージを利用

//* ジョブの権限 */
-- ジョブを作成する権限　以下の２つは当てとく方が良い。
GRANT CREATE JOB TO user1;
GRANT MANAGE SCHEDULER TO user1;

/**
  DBMS_SCHEDULERの構文
 */

--例： PROC_Aを1日毎に実行するジョブ1
BEGIN
DBMS_SCHEDULER.CREATE_JOB
(
    job_name         =>  'JOB_PROC_A',                      --ジョブの名前
    job_type         =>  'STORED_PROCEDURE',                --ジョブタイプ
    job_action       =>  'USER1.PROC_A',                    --ストアド・プロシージャ名、もしくはPL/SQLコード,
    start_date       =>  TO_DATE('2018/08/01 00:00:00',     --ジョブの開始日時
                                'yyyy/mm/dd hh24:mi:ss'),
    --end_date       =>  TO_DATE('2018/09/01 00:00:00',     --ジョブの終了日時
    --                           'yyyy/mm/dd hh24:mi:ss'),
    repeat_interval  =>  'FREQ=HOURLY',                     --ジョブの実行間隔
    enabled          =>  TRUE                               --TRUE（有効） or FALSE（無効）
);
END;
