import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа
y_min = 0
y_max = f(b)


def show_graph():
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.axhline(y=y_max, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_line = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_line / num_points)
    return np.mean(area)


if __name__ == '__main__':
    # Обчислення інтеграла
    result_spi, error = spi.quad(f, a, b)
    result_mcl = monte_carlo_integrate(f, a, b, y_min, y_max, 100_000)

    print(f"| {'Інтеграл методом': <20} | {'Результат': <10} |")
    print(f"|{'-' * 22}|{'-' * 12}|")
    print(f"| {'Scipy.quad': <20} | {result_spi:<10.7f} |")
    print(f"| {'Монте-Карло': <20} | {result_mcl:<10.7f} |")

    # show_graph()
