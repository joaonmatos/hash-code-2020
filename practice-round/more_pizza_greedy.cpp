// Copyright 2020 João Nuno Matos
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

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
