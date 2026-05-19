def ft_count_harvest_recursive(days: int | None, current: int = 1) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_count_harvest_recursive(days, current + 1)
