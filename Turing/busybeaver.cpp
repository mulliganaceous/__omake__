#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string.h>
#include <tuple>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

#define TAPESIZE 64

class TapeSegment {
private:
    int seq;
    unsigned segment[TAPESIZE];
    TapeSegment *next;
    TapeSegment *prev;
public:
    TapeSegment(int seq) {
        this->seq = seq;
        this->next = 0;
        this->prev = 0;
        std::memset(this->segment, 0, TAPESIZE*sizeof(unsigned));
    }

    TapeSegment() {
        this->seq = 0;
        this->next = 0;
        this->prev = 0;
        std::memset(this->segment, 0, TAPESIZE*sizeof(unsigned));
    }

    int getSeq() {
        return this->seq;
    }

    unsigned getColor(int pos) {
        return this->segment[pos];
    }

    void write(unsigned value, unsigned pos) {
        this->segment[pos] = value;
    }

    TapeSegment *getNext() {
        return this->next;
    }

    TapeSegment *getPrev() {
        return this->prev;
    }

    void extendLeft(TapeSegment *prev) {
        this->prev = prev;
        prev->next = this;
    }

    void extendRight(TapeSegment *next) {
        this->next = next;
        next->prev = this;
    }

    std::string toString() {
        std::stringstream ss;
        for (unsigned k : this->segment) {
            ss << k;
        }
        return ss.str();
    }
};

class Tape {
private:
    TapeSegment *leftmost, *rightmost;
    TapeSegment *start;
public:
    Tape() {
        this->start = new TapeSegment();
        this->leftmost = this->start;
        this->rightmost = this->start;
    }

    TapeSegment *getStart() {
        return this->start;
    }

    TapeSegment *getLeftmost() {
        return this->leftmost;
    }

    TapeSegment *getRightmost() {
        return this->rightmost;
    }

    void extendLeft() {
        TapeSegment *extend = new TapeSegment(this->leftmost->getSeq() - 1);
        this->leftmost->extendLeft(extend);
        this->leftmost = extend;
    }

    void extendRight() {
        TapeSegment *extend = new TapeSegment(this->rightmost->getSeq() + 1);
        this->rightmost->extendRight(extend);
        this->rightmost = extend;
    }

    std::string toString() {
        std::stringstream ss;
        for (TapeSegment *segment = this->leftmost; segment; segment = segment->getNext()) {
            ss << " " << segment->toString();
        }
        ss << "\n";
        return ss.str();
    }
};

class InstructionSet {
private:
    unsigned states;
    unsigned colors;
    std::vector<std::vector<std::tuple<unsigned, char, unsigned>>> delta;
public:
    InstructionSet(unsigned states, unsigned colors) {
        this->states = states;
        this->colors = colors;
        this->delta = std::vector<std::vector<std::tuple<unsigned, char, unsigned>>>(states, std::vector<std::tuple<unsigned, char, unsigned>>(colors, {0,0,0}));
    }

    unsigned getStates() {
        return this->states;
    }

    unsigned getColors() {
        return this->colors;
    }

    void setInstruction(unsigned state, unsigned color, unsigned writewith, unsigned transition, unsigned nextstate) {
        std::get<0>(this->delta[state - 1][color]) = writewith;
        std::get<1>(this->delta[state - 1][color]) = transition;
        std::get<2>(this->delta[state - 1][color]) = nextstate;
    }

    unsigned getWriteWith(unsigned state, unsigned color) {
        return std::get<0>(this->delta[state - 1][color]);
    }

    char getTransition(unsigned state, unsigned color) {
        return std::get<1>(this->delta[state - 1][color]);
    }

    unsigned getNextState(unsigned state, unsigned color) {
        return std::get<2>(this->delta[state - 1][color]);
    }

    std::string toString() {
        std::stringstream ss;
        ss << "\t";
        for (int k = 0; k < this->colors; k++) {
            ss << k << "\t";
        }
        ss << "\n";
        for (int state = 1; state <= this->states; state++) {
            ss << state;
            for (int color = 0; color < this->colors; color++) {
                ss << "\t" << getWriteWith(state, color) << " " << (getTransition(state, color) == -1 ? "L" : "R") << " " << getNextState(state, color);
            }
            ss << "\t\n";
        }
        return ss.str();
    }
};

class TuringMachine {
private:
    Tape *tape;
    TapeSegment *cursegment;
    InstructionSet *instructionset;
    int seq;
    int pos;
    unsigned state;
    unsigned steps;
    std::vector<unsigned> score;
    int minseq[2] = {0,0};
    int maxseq[2] = {0,0};
public:
    TuringMachine(InstructionSet *instructions) {
        this->pos = 0;
        this->seq = 0;
        this->tape = new Tape();
        this->cursegment = this->tape->getStart();
        this->instructionset = instructions;
        this->state = 1;
        this->steps = 0;
        this->score = std::vector<unsigned>(this->instructionset->getColors(), 0);
    }

    InstructionSet *getInstructionSet() {
        return this->instructionset;
    }

    void write(unsigned value) {
        unsigned color = this->getColor();
        if (color) {
            this->score[color]--;
        }
        this->cursegment->write(value, pos);
        this->score[value]++;
    }

    void moveLeft() {
        if (this->pos == 0) {
            seq--;
            pos = TAPESIZE - 1;
            if (this->seq < this->tape->getLeftmost()->getSeq()) {
                this->tape->extendLeft();
            }
            this->cursegment = this->cursegment->getPrev();
        }
        else {
            pos--;
        }
        if (this->seq < this->minseq[0]) {
            minseq[0] = this->seq;
            minseq[1] = TAPESIZE - 1;
        }
        else if (this->pos < this->minseq[1]) {
            minseq[1] = this->pos;
        }
    }

    void moveRight() {
        if (this->pos == TAPESIZE - 1) {
            seq++;
            pos = 0;
            if (this->seq > this->tape->getRightmost()->getSeq()) {
                this->tape->extendRight();
            }
            this->cursegment = this->cursegment->getNext();
        }
        else {
            pos++;
        }
        if (this->seq > this->maxseq[0]) {
            maxseq[0] = this->seq;
            maxseq[1] = 0;
        }
        else if (this->pos > this->maxseq[1]) {
            maxseq[1] = this->pos;
        }
    }

    unsigned getState() {
        return this->state;
    }

    unsigned getColor() {
        return this->cursegment->getColor(this->pos);
    }

    unsigned getSeq() {
        return this->seq;
    }

    unsigned getPos() {
        return this->pos;
    }

    unsigned getSteps() {
        return this->steps;
    }

    Tape *getTape() {
        return this->tape;
    }

    TapeSegment *getSegment() {
        return this->cursegment;
    }

    int *getMinseq() {
        return this->minseq;
    }

    int *getMaxseq() {
        return this->maxseq;
    }

    std::vector<unsigned> getScore() {
        return this->score;
    }

    unsigned step() {
        if (!state) {
            return 0;
        }
        unsigned color = this->getColor();
        unsigned nextstate = this->instructionset->getNextState(this->state, this->getColor());

        this->write(this->instructionset->getWriteWith(this->state, color));
        char direction = this->instructionset->getTransition(this->state, color);
        if (direction == 1) {
            this->moveRight();
        }
        else if (direction == -1) {
            this->moveLeft();
        }
        this->state = nextstate;
        steps++;
        return this->state;
    }

    std::string toString() {
        std::stringstream ss;
        for (TapeSegment *segment = this->tape->getLeftmost(); segment; segment = segment->getNext()) {
            int diff = this->seq - segment->getSeq();
            if (diff*diff < 4) {
                for (int k = 0; k < TAPESIZE; k++) {
                    if (this->seq == segment->getSeq() && k == this->pos) {
                        ss << "{" << segment->getColor(k) << "}";
                    }
                    else {
                        ss << " " << segment->getColor(k) << " ";
                    }
                }
                ss << " ";
            }
        }
        ss << "\tState: " << this->state << "\tPosition: " << this->seq << "~" << this->pos << "\n";
        return ss.str();
    }
};

// int main() {
//     InstructionSet *instructions = new InstructionSet(5, 2);
//     instructions->setInstruction(1,0,1,-1,2);
//     instructions->setInstruction(1,1,1,+1,3);
//     instructions->setInstruction(2,0,1,-1,3);
//     instructions->setInstruction(2,1,1,-1,2);
//     instructions->setInstruction(3,0,1,-1,4);
//     instructions->setInstruction(3,1,0,+1,5);
//     instructions->setInstruction(4,0,1,+1,1);
//     instructions->setInstruction(4,1,1,+1,4);
//     instructions->setInstruction(5,0,0,0,0);
//     instructions->setInstruction(5,1,0,+1,1);

//     std::cout << instructions->toString();
//     TuringMachine *busybeaver = new TuringMachine(instructions);
//     std::cout << busybeaver->toString();
//     for (int k = 0; true && busybeaver->getState(); k++) {
//         busybeaver->step();
//         if (k % 1000000 == 0)
//             std::cout << busybeaver->toString() << "\n";
//     }
//     std::cout << "S:\t" << busybeaver->getSteps() << "\n";
//     std::cout << "Seq:\t" << busybeaver->getMinseq()[0]*TAPESIZE + busybeaver->getMinseq()[1] << " ~ " << busybeaver->getMaxseq()[0]*TAPESIZE + busybeaver->getMaxseq()[1] << "\n";
//     for (int k = 0; k < 2; k++) {
//         std::cout << k << ":\t" << busybeaver->getScore()[k] << "\n";
//     }
//     return 0;
// }