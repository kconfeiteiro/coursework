!
! diff2d.f90 - Simulates two-dimensional diffusion on a square domain
!              Fortran 90 version
!
!
program diffusion_2d
    implicit none
    ! Include file sets parameters D, x1, x2, runtime, dx, outtime, and graphics:
    logical, parameter :: False=.false., True=.true.
    real*8  :: D, x1, x2, runtime, dx, outtime, dt, simtime, a, b
    logical :: graphics
    integer :: Nx, Ny, npnts, nsteps, nper, i, j, s
    real*8, allocatable, dimension(:)             :: x
    real*8, allocatable, dimension(:,:)           :: laplacian
    real*8, pointer, dimension(:,:)               :: u, u_next, tmp
    real*8, target, allocatable, dimension(:,:,:) :: u_buffer
    real*8  :: tstart, tend
    include 'diff2dparams.py'

    ! Compute derived parameters.
    Nx     = floor((x2-x1)/dx) ! number of x points
    Ny     = Nx           ! number of y points, same as x in this case.
    npnts  = Nx + 2       ! number of x points including boundary points
    dx     = (x2-x1)/Nx   ! recomputed (previous dx may not fit in [x1,x2])
    dt     = 0.25*dx**2/D    ! time step size (edge of stability)
    nsteps = int(runtime/dt) ! number of steps of that size to reach runtime
    nper   = int(outtime/dt) ! how many step s between snapshots
    if (nper == 0) then
       nper = 1
    endif
    ! Allocate arrays.
    allocate(x(npnts))
    allocate(u_buffer(npnts,npnts,2))
    allocate(laplacian(npnts,npnts))
    u => u_buffer(:,:,1)
    u_next => u_buffer(:,:,2)
    ! Initialize.
    do i=1,npnts 
       x(i) = x1+((i-2)*(x2-x1))/Nx ! x values (also y values)
    enddo
    u=0.0
    u_next=0.0
    simtime=0*dt
    do i=2,npnts-1
        a = 1 - abs(1 - 4*abs((x(i)-(x1+x2)/2)/(x2-x1)))
        do j=2,npnts-1
            b = 1 - abs(1 - 4*abs((x(j)-(x1+x2)/2)/(x2-x1)))
            u(i,j) = a*b
        end do
    end do
    ! Output initial signal.
    print '(" at t =  ", f5.2 )', simtime    
    if (graphics .eqv. .true.) then
       do i=1,npnts
          do j=1,npnts
             write(7,*) x(i), x(j), u(i,j)
          enddo
       enddo
    endif
    call cpu_time(tstart)
    ! Let temporary array hold laplacian.
    laplacian = 0.0 
    do s=1,nsteps
        ! Take one time step to produce new density.
        ! Using explicit iterations over indices instead
        do j=2,Ny+1
            do i=2,Nx+1
                laplacian(i,j) = u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1)-4*u(i,j)
            end do
        end do
        do j=2,Ny+1
            do i=2,Nx+1
                u_next(i,j) = u(i,j) + (D/dx**2)*dt*laplacian(i,j)
            end do
        end do
        ! Swap array pointers so t+1 becomes the new t, and update simulation time.
        tmp => u
        u => u_next
        u_next => tmp
        simtime = simtime + dt
        ! Plot and report time.
        if (mod(s,nper) == 0) then
            print '(" at t =  ", f5.2 )', simtime    
            if (graphics .eqv. .true.) then
               do i=1,npnts
                  do j=1,npnts
                     write(11,*) x(i), x(j), u(i,j)
                  enddo
               enddo
               write(11,*)
        !        call plotdens(dens, x(1), x(npnts), .false.)
            endif
        endif
    enddo
    if (graphics .eqv. .true.) then
       do i=1,npnts
          do j=1,npnts
             write(11,*) x(i), x(j), u(i,j)
          enddo
       enddo
    endif
    call cpu_time(tend)
    print '("Simulation finished in ", f16.12," s")', tend-tstart    
end program diffusion_2d

