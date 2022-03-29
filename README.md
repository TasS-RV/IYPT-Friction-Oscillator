# IYPT-Friction-Oscillator
33rd International Young Physicist's Tournament - Friction Oscillator Data Analysis Code.

**Transferred into Github Repo for Storage as of 03/22**

**Last edits to files were made 01/21**


1)The 'main' directory includes files that can be executed to analyse the text files - the text files are generated from Matlab image processing software that automatically wrote into text files.

Matlab was used initially for breaking down videos of the Friction Oscillator into individual frames, then finding the displacement of a flourescent or coloured marker taped to the centre of the rod with reference to initial pixel position. (Not present in the python files).

2)The 'graphs' directory shows some of the results that were obtained.

3)The 'files' directory contains all of the text files form data accumulated over a variety of materials for the 'massive' rod.

For further details regarding the proposed problem, please view:
https://iypt.org/wp-content/uploads/2019/07/IYPT_2020_Problems.pdf

For images of the development process of the experiement, please see the image and video gallery in:
https://drive.google.com/drive/folders/12KxbCc4MCo_gYfqAGECJBr5q1T7iRK5y?usp=sharing

The files in main are intended to run by: entering a file name, or a list of filenames of the .txt files storing the data collated form Matlab, and performaing statistical analysis on them before a visual display of the behaviour of the 'run' as a pyplot graph. In some cases, where the data was considered sufficiently clean, it has been smoothened out, with 'attempt' at polyfit interpolation of the results to model the behaviour.





