class Train:
    def __init__(self, train_id, arrival_time, departure_time):
        self.train_id = train_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time


def allocate_platform(trains):
    trains.sort(key=lambda train: train.arrival_time)
    platforms = {}  # Platform number to train mapping
    platform_count = 0

    for train in trains:
        allocated = False
        for platform, last_train in platforms.items():
            if train.arrival_time >= last_train.departure_time:
                platforms[platform] = train
                print(
                    f"Train {train.train_id} allocated to Platform {platform}")
                allocated = True
                break

        if not allocated:
            platform_count += 1
            platforms[platform_count] = train
            print(
                f"Train {train.train_id} allocated to New Platform {platform_count}")


# Example usage
trains = [Train(1, 8, 11), Train(2, 10, 13), Train(3, 12, 14), Train(4, 9, 12)]
allocate_platform(trains)
