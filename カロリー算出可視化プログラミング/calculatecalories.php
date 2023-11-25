<?php
// カロリー計算関数
function calculateCalories($trainingCalories, $mealCalories, $bmrCalories) {
    return $mealCalories - $bmrCalories + $trainingCalories;
}

$trainingCalories = $_POST['training_calories']; // トレーニングで消費したカロリー
$mealCalories = $_POST['meal_calories']; // 食事で摂取したカロリー

// ユーザーの基本情報をもとに基礎代謝カロリーを算出
$bmrCalories = calculateBMR($_POST['age'], $_POST['gender'], $_POST['weight'], $_POST['height']);


$totalCalories = calculateCalories($trainingCalories, $mealCalories, $bmrCalories);


echo "トレーニングで消費したカロリー: $trainingCalories kcal<br>";
echo "食事で摂取したカロリー: $mealCalories kcal<br>";
echo "基礎代謝カロリー: $bmrCalories kcal<br>";
echo "合計カロリー: $totalCalories kcal<br>";
