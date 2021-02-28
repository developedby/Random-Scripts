// Comparing time.h's time() to perf_event.h's PERF_COUNT_SW_TASK_CLOCK
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <linux/perf_event.h>
#include <linux/hw_breakpoint.h>
#include <sys/syscall.h>
#include <sys/ioctl.h>

void main() {
    // Setting up the perf fd
    struct perf_event_attr pe;
    memset(&pe, 0, sizeof(struct perf_event_attr));
    pe.type = PERF_TYPE_SOFTWARE;
    pe.size = sizeof(struct perf_event_attr);
    pe.config = PERF_COUNT_SW_TASK_CLOCK;
    pe.disabled = 1;
    pe.exclude_kernel = 1;
    pe.exclude_hv = 1;
    // glibc doesn't expose perf_event_open, so directly calling the syscall
    int fd = syscall(__NR_perf_event_open, &pe, 0, -1, -1, 0);
    ioctl(fd, PERF_EVENT_IOC_RESET, 0);
    ioctl(fd, PERF_EVENT_IOC_ENABLE, 0);

    // For comparing with a known unit
    time_t time_start = time(0);
    long long count_start;
    read(fd, &count_start, sizeof(long long));

    // Very long calculation
    int a = 1;
    for (int i=0; i<1000000; i++)
        for (int j=0; j<10000; j++)
            a++;

    // Results
    ioctl(fd, PERF_EVENT_IOC_DISABLE, 0);
    long long count_finish;
    read(fd, &count_finish, sizeof(long long));
    time_t time_finish = time(0);

    printf("time(): %d\n", time_finish-time_start);
    printf("PERF_COUNT_SW_TASK_CLOCK: %lld\n", count_finish-count_start);
    return;
}
