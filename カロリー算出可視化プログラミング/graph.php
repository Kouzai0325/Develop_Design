<?php
require_once ('jpgraph/jpgraph.php');
require_once ('jpgraph/jpgraph_pie.php');

$protein = $_POST['protein'];
$fat = $_POST['fat'];
$carbohydrate = $_POST['carbohydrate'];

// データを配列に格納
$data = array($protein, $fat, $carbohydrate);

// グラフを生成
$graph = new PieGraph(400, 300);
$graph->SetShadow();

// データをセット
$p1 = new PiePlot($data);
$graph->Add($p1);

// グラフを出力
$graph->Stroke();
