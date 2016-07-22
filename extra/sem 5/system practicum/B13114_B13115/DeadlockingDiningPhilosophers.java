import java.util.concurrent.*;
import java.util.*;

class forks {

    private boolean check = false;

    public synchronized
            void take() throws InterruptedException {
        while (check) {
            wait();
        }
        check = true;
    }

    public synchronized void drop() {
        check = false;
        notifyAll();
    }
}

class Philosopher implements Runnable {

    private final forks left;
    private final forks right;
    private final int id;
    private final int ponderFactor;
    private final Random rand = new Random(47);

    private void pause() throws InterruptedException {
        if (ponderFactor == 0) {
            return;
        }
        TimeUnit.MILLISECONDS.sleep(
                rand.nextInt(ponderFactor * 250));
    }

    public Philosopher(forks left, forks right,
            int ident, int ponder) {
        this.left = left;
        this.right = right;
        id = ident;
        ponderFactor = ponder;
    }

    public void run() {
        try {
            while (!Thread.interrupted()) {
                System.out.println(this + " " + "thinking");
                pause();
                // Philosopher becomes hungry
                System.out.println(this + " " + "grabbing right");
                right.take();
                System.out.println(this + " " + "grabbing left");
                left.take();
                System.out.println(this + " " + "eating");
                pause();
                right.drop();
                left.drop();
            }
        } catch (InterruptedException e) {
            System.out.println(this + " " + "exiting");
        }
    }

    public String toString() {
        return "Philosopher " + id;
    }
}

public class DeadlockingDiningPhilosophers {

    public static void main(String[] args) throws Exception {
        int ponder = 5;
        if (args.length > 0) {
            ponder = Integer.parseInt(args[0]);
        }
        int size = 5;
        if (args.length > 1) {
            size = Integer.parseInt(args[1]);
        }
        ExecutorService exec = Executors.newCachedThreadPool();
        forks[] sticks = new forks[size];
        for (int i = 0; i < size; i++) {
            sticks[i] = new forks();
        }
        for (int i = 0; i < size; i++) {
            exec.execute(new Philosopher(
                    sticks[i], sticks[(i + 1) % size], i, ponder));
        }
        if (args.length == 3 && args[2].equals("timeout")) {
            TimeUnit.SECONDS.sleep(1);
        } else {
            System.out.println("Press 'Enter' to quit");
            System.in.read();
        }
        exec.shutdownNow();
    }
}

