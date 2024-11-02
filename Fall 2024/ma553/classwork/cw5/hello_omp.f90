PROGRAM hello_omp
    IMPLICIT NONE
    INTEGER :: NTHREADS, TID
    INTEGER :: OMP_GET_NUM_THREADS, OMP_GET_THREAD_NUM
    !Fork a team of threads with each thread having a private TID variable
    !$OMP PARALLEL PRIVATE(TID)
    ! Obtain and print thread id
    TID = OMP_GET_THREAD_NUM()
    write(*,'(a,i3,a)')' Thread ', TID, ' says "Hello, world!"'
    ! Only master thread does this
    IF (TID .EQ. 0) THEN
            NTHREADS = OMP_GET_NUM_THREADS()
            write(*,'(a,i2,a)')' Master Thread: running with ',NTHREADS,' threads'
    END IF
    !All threads join master thread and disband
    !$OMP END PARALLEL
END PROGRAM hello_omp
