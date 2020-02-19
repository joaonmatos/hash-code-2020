#include <iostream>
#include <stack>

int main() {
    int max_no_slices;
    int no_pizza_types;
    std::cin >> max_no_slices >> no_pizza_types;
    std::cin.ignore(INT32_MAX, '\n');

    int pizzas[no_pizza_types];
    for (int i = 0; i < no_pizza_types; i++) {
        int pizza;
        std::cin >> pizza;
        pizzas[i] = pizza;
    }

    std::stack<int> selected_pizzas;
    int selected_slices = 0;
    for (int i = no_pizza_types - 1; i >= 0; i--) {
        int pizza = pizzas[i];
        if (pizza <= max_no_slices - selected_slices) {
            selected_pizzas.push(i);
            selected_slices += pizza;
        }
    }

    std::cout << selected_pizzas.size() << std::endl;
    while (!selected_pizzas.empty()) {
        std::cout << selected_pizzas.top() << ' ';
        selected_pizzas.pop();
    }
    std::cout << std::endl;

    return 0;
}
