<?php

session_start();

// Function to add an expense
function addExpense($category, $amount) {
    $_SESSION['expenses'][] = [
        'category' => $category,
        'amount' => $amount,
        'date' => date('Y-m-d H:i:s')
    ];
}

// Initialize expenses if not set
if (!isset($_SESSION['expenses'])) {
    $_SESSION['expenses'] = [];
}

while (true) {
    echo "\nOptions:\n1. Add Expense\n2. View Expenses\n3. Total Expenses\n4. Exit\nChoose an option: ";
    $choice = trim(fgets(STDIN));

    switch ($choice) {
        case '1':
            echo "Enter expense category: ";
            $category = trim(fgets(STDIN));
            echo "Enter expense amount: ";
            $amount = trim(fgets(STDIN));
            
            if (!is_numeric($amount) || $amount <= 0) {
                echo "Invalid amount. Please enter a positive number.\n";
                break;
            }
            
            addExpense($category, $amount);
            echo "Expense added successfully!\n";
            break;

        case '2':
            if (empty($_SESSION['expenses'])) {
                echo "No recorded expenses.\n";
            } else {
                echo "\nRecorded Expenses:\n";
                foreach ($_SESSION['expenses'] as $index => $expense) {
                    echo ($index + 1) . ". {$expense['category']} - \${$expense['amount']} ({$expense['date']})\n";
                }
            }
            break;

        case '3':
            $total = array_sum(array_column($_SESSION['expenses'], 'amount'));
            echo "Total Expenses: \$$total\n";
            break;

        case '4':
            echo "Goodbye!\n";
            exit;

        default:
            echo "Invalid option. Please try again.\n";
    }
}
