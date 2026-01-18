public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven() {
        return 40;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int t) {
        return 40-t;
    } 

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int l) {
        return l*2;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int l, int t) {
        return l*2 + t;
    }
}
