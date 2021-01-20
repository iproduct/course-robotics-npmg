"""
Задача 2.  Два града A и B са на разстояние d километра. 
В едно и също време от всеки град тръгва бърз влак в посока към другия. 
Скоростта на влака тръгнал от град A е v1 км/ч, а скоростта на влака тръгнал от град B е v2 км/ч.
Едновременно с тръгването на влака от град А излита изключително бърза муха, 
която лети срещу влака тръгнал от град B със скорост v км/ч. При срещата с този влак, 
мухата прави обратен завой и започва да лети към влака идващ от град А. Когато го срещне, тя 
полетява в обратна посока и продължава така, докато влаковете се срещнат (разстоянието между тях стане равно на дължината на  мухата  ɛ).

Да се напише програма, която по въведени d, v, v1, v2 и ɛ, намира и отпечатва:
1) дължините на различните участъци от пътя, които мухата ще прелети;
2) общото разстояние, което ще прелети мухата.
"""

def fly_bug(distance, bug_speed, train1_speed, train2_speed, bug_size):
    if bug_speed < train1_speed:
        total_train_speed = train1_speed + train2_speed
        time_till_collision = distance / total_train_speed # maybe use bug_size here?
        bug_covered_distance = time_till_collision * bug_speed
        print("The fly will never surpass the train and will cover distance:", bug_covered_distance)
        return bug_covered_distance

    if abs(distance) < abs(bug_size):
        print("The trains met")
        return 0 
    
    bug_plus_opposite_train_speed = bug_speed + train2_speed
    time_bug_to_meet_train2 = distance / bug_plus_opposite_train_speed

    bug_travel_distance = time_bug_to_meet_train2 * bug_speed
    print("The bug covered distance:", bug_travel_distance)
    reduced_train_distance = distance - train1_speed * time_bug_to_meet_train2 - train2_speed * time_bug_to_meet_train2
    # Swap the two trains
    return bug_travel_distance + fly_bug(reduced_train_distance, bug_speed, train2_speed, train1_speed, bug_size)

def fly_bug_wrapper(distance, bug_speed, train1_speed, train2_speed, bug_size):
    total_bug_distance = fly_bug(distance, bug_speed, train1_speed, train2_speed, bug_size)
    print("The bug covered total of:", total_bug_distance)

if __name__ == '__main__':
    fly_bug_wrapper(100, 50, 5, 15, 0.01)
