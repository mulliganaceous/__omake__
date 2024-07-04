/*
 * GL01Hello.cpp: Test OpenGL/GLUT C/C++ Setup
 * Tested under Eclipse CDT with MinGW/Cygwin and CodeBlocks with MinGW
 * To compile with -lfreeglut -lglu32 -lopengl32
 */
#include <GL/glut.h>  // GLUT, include glu.h and gl.h
#include "busybeaver.cpp" 
#include <unistd.h>

/* Color mapping */
float colormap[6][3] = {{1.0f,1.0f,1.0f},
                        {233.f/255.f,61.f/255.f,105.f/255.f},
                        {61.f/255.f,233.f/255.f,87.f/255.f},
                        {61.f/255.f,174.f/255.f,233.f/255.f},
                        {232.f/255.f,203.f/255.f,45.f/255.f},
                        {233.f/255.f,120.f/255.f,61.f/255.f},};

/* Handler for window-repaint event. Call back when the window first appears and
   whenever the window needs to be re-painted. */
void display() {
    InstructionSet *instructions = new InstructionSet(5, 2);
    instructions->setInstruction(1,0,1,-1,2);
    instructions->setInstruction(1,1,1,+1,3);
    instructions->setInstruction(2,0,1,-1,3);
    instructions->setInstruction(2,1,1,-1,2);
    instructions->setInstruction(3,0,1,-1,4);
    instructions->setInstruction(3,1,0,+1,5);
    instructions->setInstruction(4,0,1,+1,1);
    instructions->setInstruction(4,1,1,+1,4);
    instructions->setInstruction(5,0,0,0,0);
    instructions->setInstruction(5,1,0,+1,1);

    std::cout << instructions->toString();
    TuringMachine *busybeaver = new TuringMachine(instructions);
    std::cout << busybeaver->toString();
    usleep(15000000);

    // OMG    
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Set background color to black and opaque
    glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
    int i = 0;
    int period = 64;
    int fps = 2;
    while (busybeaver->getState())
    {
        // Turing machine
        std::cout << "\r" << "State:\t" << busybeaver->getState() << "\n";
        std::cout << "\r" << "S:\t" << busybeaver->getSteps() << "\n";
        std::cout << "\r" << "X:\t" << (int)(busybeaver->getSeq()*TAPESIZE + busybeaver->getPos()) << "\n";
        for (int k = 0; k < 2; k++) {
            std::cout << "\r" << k << ":\t" << busybeaver->getScore()[k] << "\n";
        }
        // Draw a Red 1x1 Square centered at origin
        float s = 1.0f / period;
        unsigned color = busybeaver->getColor();
        int increase = busybeaver->getInstructionSet()->getWriteWith(busybeaver->getState(), color) != color;
        Tape *tape = busybeaver->getTape();
        glBegin(GL_QUADS);
        for (TapeSegment *segment = tape->getLeftmost(); segment; segment = segment->getNext())
        {
            for (int pos = 0; pos < TAPESIZE; pos++)
            {
                int k = (1 + segment->getSeq())*TAPESIZE + pos;
                char thisposition = segment->getSeq() != busybeaver->getSeq() || pos != busybeaver->getPos();
                if (segment->getColor(pos) == 1 || !thisposition)
                {
                    int colorindex = 0;
                    if (!thisposition) {
                        colorindex = busybeaver->getState();
                    }
                    glColor3f(colormap[colorindex][0], colormap[colorindex][1], colormap[colorindex][2]);
                    glVertex2f(-1.f + k * s, 1.f - i * s); // x, y
                    glVertex2f(-1.f + (k + 1) * s, 1.f - i * s);
                    glVertex2f(-1.f + (k + 1) * s, 1.f - (i + 1) * s);
                    glVertex2f(-1.f + k * s, 1.f - (i + 1) * s);
                }
            }
        }

        s = 1.0f / TAPESIZE * 2;
        TapeSegment *segment = busybeaver->getSegment();
        for (int pos = 0; pos < TAPESIZE; pos++)
        {
            char thisposition = segment->getSeq() != busybeaver->getSeq() || pos != busybeaver->getPos();
            if (!thisposition) {
                int colorindex = busybeaver->getState();
                glColor3f(colormap[colorindex][0], colormap[colorindex][1], colormap[colorindex][2]);
            }
            else {
                char color = segment->getColor(pos);
                glColor3f(color, color, color);
            }
            glVertex2f(-1.f + pos * s, -1.f); // x, y
            glVertex2f(-1.f + (pos + 1) * s, -1.f);
            glVertex2f(-1.f + (pos + 1) * s, -1.f + s);
            glVertex2f(-1.f + pos * s, -1.f + s);
        }

        glEnd();
        busybeaver->step();

        if (increase) {
            i += increase;
            i %= (2*period*127/128);
            if (!i) {
                glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Set background color to black and opaque
                glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
                period *= 2;
                fps *= 4;
            }
        }

        glFlush();
        usleep(1E6/fps);
    }
}
 
/* Main function: GLUT runs as a console application starting at main()  */
int main(int argc, char** argv) {
    glutInitWindowSize(1024, 1024);   // Set the window's initial width & height
    glutInit(&argc, argv);                 // Initialize GLUT
    glutCreateWindow("Busy Beaver game"); // Create a window with the given title
    
    glutDisplayFunc(display); // Register display callback handler for window re-paint
    glutMainLoop();           // Enter the event-processing loop
    return 0;
}