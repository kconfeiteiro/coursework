!++++++++++++++++   compile with gfortran Kahan.f   ++++++++++++++++++++
!=======================================================================
!      W. Kahan's example of finite precision arithmetic failings 
!  from C. Van Loan, Intro. to Computational Science, 1995; p.xxiv     
!####&###1#########2#########3#########4#########5#########6#########7##
         program Kahan
         
         implicit none 
         real :: h, x, y, u, v, q
         !double precision :: h, x, y, u, v, q
         
         h=1.0/2
         x=2.0/3 - h 
         y=3.0/5 - h 
         u=(x+x+x) - h
         v=(y+y+y+y+y) - h
         q=u/v 

         write(*,*) 
         write(*,*)'Fortran:' 
         write(*,*) 'h =', h
         write(*,*) 'x =', x
         write(*,*) 'y =', y
         write(*,*) 'u =', u
         write(*,*) 'v =', v
         write(*,*) 'q =', q
         write(*,*) 

        stop

      end program kahan 
!_______________________________________________________________________
!####&###1#########2#########3#########4#########5#########6#########7##
