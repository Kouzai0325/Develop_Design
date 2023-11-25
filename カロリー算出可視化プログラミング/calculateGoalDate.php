<?php
// 目標までの日時計算関数
function calculateGoalDate($targetCalories, $currentCalories, $burnedCaloriesPerDay) {
    $daysRemaining = ($targetCalories - $currentCalories) / $burnedCaloriesPerDay;
    return date('Y-m-d', strtotime("+$daysRemaining days"));
}


$targetCalories = $_POST['target_calories'];
$burnedCaloriesPerDay = $_POST['burned_calories_per_day'];

// 現在のカロリーを計算
$currentCalories = calculateCalories($trainingCalories, $mealCalories, $bmrCalories);

// 目標までの日時を計算
$goalDate = calculateGoalDate($targetCalories, $currentCalories, $burnedCaloriesPerDay);

// 結果を出力
echo "現在の合計カロリー: $currentCalories kcal<br>";
echo "目標までの日時: $goalDate";
