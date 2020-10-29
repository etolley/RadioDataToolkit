#include <stdlib.h>
#include <stdio.h>

#define CHECK
#define POSIX_CHECK

int main ( const int argc, const char * const argv[])
{
    if (argc != 11 && argc != 12)
    {
        fprintf(stderr,
                "usage: %s <path/to/raw> "
                "<xsize-source> <ysize-source> <zsize-source> "
                "<xstart-roi> <ystart-roi> <zstart-roi> "
                "<xsize-roi> <ysize-roi> <zsize-roi> "
                "[<path/to/out>]\n",
                argv[0]);

        return EXIT_FAILURE;
    }

    const char * const pathname_src = argv[1];

    FILE * fin;
    POSIX_CHECK(fin = fopen(pathname_src, "rb"));

    const int xsize = atoi(argv[2]);
    const int ysize = atoi(argv[3]);
    const int zsize = atoi(argv[4]);

    const int xs = atoi(argv[5]);
    const int ys = atoi(argv[6]);
    const int zs = atoi(argv[7]);

    POSIX_CHECK(0 == fseek(fin, 0, SEEK_END));

    const size_t filesize = ftell(fin);

    CHECK(filesize % (xsize * (size_t) ysize * (size_t) zsize) == 0,
          "error: invalid source sizes\n");

    const size_t wordsize = filesize/(xsize*(size_t) ysize * (size_t) zsize);

    rewind(fin);

    const int xn = atoi(argv[8]);
    const int yn = atoi(argv[9]);
    const int zn = atoi(argv[10]);

    FILE * fout = stdout;

    if (argc == 12) POSIX_CHECK(fout = fopen(argv[11], "wb"));

    const size_t sizeofline = xn * wordsize;
    unsigned char * line = malloc(xn * wordsize);

    for(int zi = zs; zi < zs + zn; ++zi)
        for(int yi = ys; yi < ys + yn; ++yi)
        {
            POSIX_CHECK(0 == fseek(fin, wordsize * ((size_t)xs + xsize * ((size_t)yi + ysize * (size_t)zi)), SEEK_SET));

            int n = fread(line, sizeofline, 1, fin);

            CHECK(1 == n, "error: could not read an x-line\n");

            n = fwrite(line, sizeofline, 1, fout);

            CHECK(1 == n, "error: could not write an x-line\n");
        }

    free(line);

    if (fout != stdout) POSIX_CHECK(0 == fclose(fout));

    POSIX_CHECK(0 == fclose(fin));

    return EXIT_SUCCESS;
}