# 3-1
- 同じような処理を冗長に繰り返し書く必要性がなくなるため
- 模範解答 : 関数を用いれば、コードの重複を減らせます。その結果、プログラムが短く、読みやすく、更新しやすくなります。

# 3-2
- 関数の中のコードは関数が呼び出されたときに実行される
- 模範解答 : 関数の中のコードは、関数が呼び出されると実行されます。関数が定義されたときには呼び出されません。

# 3-3
- 関数を定義する文はdef文である
- 模範解答 : 関数を定義する(つまり作成する)のは、def文。

# 3-4
- 関数 : 特定の処理をひとまとまりにしたもの
- 関数呼び出し : 関数を実行すること
- 模範解答 : 関数は、def文とdef節のコードから構成されています。関数呼び出しは、プログラム実行を関数の中に移し、関数の戻り地を返します。

# 3-5
- グローバルスコープ : 1つ
- ローカルスコープ : ブロックの数
- 模範解答 : グローバルスコープは1つ。ローカルスコープは関数が呼び出されるたびに作られるので無数にあります。

# 3-6
- 関数から変えると、ローカルスコープ内の変数は無くなる
- 模範解答 : 関数から変えると、ローカルスコープは破棄され、その中の変数はすべて忘れ去られます。

# 3-7
- 戻り値は関数からreturn文で返される値
- 戻り地は式の一部になりえる
- 模範解答 : 戻り値とは関数呼び出しが評価される値です。他の値と同様に、戻り地は式の一部になりえます。

# 3-8
- 関数がreturn文を持たない場合、関数の戻り値は暗黙でNoneになる
- 模範解答 : 関数にreturn文がなければ、戻り値はNoneになります。

# 3-9
- 関数の中でグローバル変数を参照するには、変数名の前にglobalをつける
- 模範解答 : 関数にグローバル変数を参照するように指定するには、global文を用います。

# 3-10
- Noneのデータ型はObject型
- 模範解答 : Noneのデータ型はNoneType

# 3-11
- ライブラリまたは実行pythonディレクトリにある areallyourpetsnamederic.py 内の関数を利用できるようにする
- 模範解答 : このimport文は、areallyournamedericという名前のモジュールをインポートします(実際にはこんな名前のPythonモジュールは存在しない)。

# 3-12
- spam.bacon() で呼び出す
- 模範解答 : この関数は、spam.bacon()のように呼び出します。

# 3-13
- try文のブロックに異常終了になりうる部分を含め、except文で異常終了になりうるエラー名を記述し、そのブロックで異常終了処理を記述する。
- 模範解答 : エラーを起こしそうなコードを、try節の中に置きます。

# 3-14
- try節 : 異常終了を検知する
- except節 : 異常終了処理を行う
- 模範解答 : 潜在的にエラーになりうるコードはtry節に書きます。エラーが起こったときに実行するコードはexcept節に置きます。
