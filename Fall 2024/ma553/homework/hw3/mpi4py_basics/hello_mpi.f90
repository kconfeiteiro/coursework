! This code shows the 4 basic MPI routines: 
!    MPI_INIT 
!    MPI_FINALIZE
!    MPI_COMM_RANK
!    MPI_COMM_SIZE
!
!---------------------------------------------------------------

PROGRAM hello_mpi 

      use mpi

      IMPLICIT NONE

      INTEGER :: Pid, Nproc, ierr

      CALL MPI_INIT( ierr )
      CALL MPI_COMM_RANK( MPI_COMM_WORLD, Pid, ierr )
      CALL MPI_COMM_SIZE( MPI_COMM_WORLD, Nproc, ierr )
      !PRINT *, "Hello World! I am process ",Pid," of total ",Nproc, " processes"
      if ( Pid .EQ. 0 ) then
   		write ( *, '(a,i3,a)' ) ' Master: No. of processes =',Nproc ! Print a message.
	end if
	write ( *, '(a,i3,a)' ) ' Process ', Pid, ' says "Hello, world!"'
      CALL MPI_FINALIZE(ierr)

END PROGRAM hello_mpi 
