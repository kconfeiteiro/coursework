! FILE: pingpong.f90
!
! This is an example program intended to demonstrate
! the use of simple send and receive commands.  Each
! of 2 CPUs sends its ID bufsize to the other one and
! at the end they both print the values of what they 
! sent as well as what they received.
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 PROGRAM pingpong

      USE MPI   

      IMPLICIT NONE


      INTEGER :: me, sbuf, rbuf, ierr
      INTEGER, DIMENSION (MPI_STATUS_SIZE) :: status
      INTEGER :: bufsize, dest, source, tag, Nproc, icode

! initialize MPI
      CALL MPI_INIT(ierr)
      CALL MPI_COMM_RANK( MPI_COMM_WORLD, me, ierr )
      CALL MPI_COMM_SIZE( MPI_COMM_WORLD, Nproc, ierr )

        IF(Nproc.NE.2) THEN
                PRINT *, "Please run me on 2 MPI tasks. Thanks!"
                CALL MPI_ABORT(MPI_COMM_WORLD,icode,ierr)
        END IF

! set an ID value for the message tag 

      tag=99

! have the first task [task zero] send then receive

      IF (me.EQ.0) THEN

! set values for the send command
!    dest is where the message is going
!    bufsize is the bufsize of items being sent

         dest=1
         bufsize=1

! set values for the recv command
!     source is where to expect a message from

         source=1

! send a message containing the task bufsize to task 1
! place the task ID in the variable sbuf
	 sbuf = me

         CALL MPI_SEND(sbuf, bufsize, MPI_INTEGER, dest, tag, & 
              MPI_COMM_WORLD, ierr)

! receive the message from task 1 into rbuf

         CALL MPI_RECV(rbuf, bufsize, MPI_INTEGER, source, tag, &
              MPI_COMM_WORLD, status, ierr)

      END IF

! have the second task [task one] receive then send.  This constitutes
!    "blocking" message passing.

      IF (me.EQ.1) THEN

! set values for the send command
!    dest is where the message is going
!    bufsize is the bufsize of items being sent

         dest=0
         bufsize=1

! set values for the recv command
!     source is where to expect a message from

         source=0

! Receive the message from task 0 into rbuf

         CALL MPI_RECV(rbuf, bufsize, MPI_INTEGER, source, tag,  &
              MPI_COMM_WORLD, status, ierr)

! Send a message containing the task bufsize to task 0
! place the task ID in the variable sbuf

         sbuf = me
         CALL MPI_SEND(sbuf, bufsize, MPI_INTEGER, dest, tag,   &
              MPI_COMM_WORLD, ierr)

      END IF

! have each task print both what it sent and received

      PRINT*, "TASK #", me, " sent ", sbuf
      PRINT*, "TASK #", me, " received ", rbuf 

! close out MPI
      CALL MPI_FINALIZE(ierr)

 END PROGRAM pingpong
