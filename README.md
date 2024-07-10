<h1>Info</h1>

<p>"Light Cutter" is a program that can cut light from a photo, provided that you have a photo that does not have light on it. The main task was to cut out light from Blender renders to then use them in 2D games.</p>
<p>To install the application there are two options: 
  <ol>
    <li>Download Light Cutter.exe and run it.</li>
    <li>Download files from "src" and run main.py (make sure image.py is in the same directory as main.py).</li>
  </ol>
</p>
<p>To get started, upload an image with and without light (they must be the same size), then click on the "Render and save" button, wait a little bit (it depends on the size of the images) and save it in the directory you need.</p>


<h1>Examples of work</h1>

<table border=0>
  <tr>
    <th>Input 1 (with Light)</th>
    <th>Input 2 (without Light)</th>
    <th>Output (Result)</th>
    <th>Animation</th>
  </tr>

  <tr><td colspan=3><b>Example #1 (one point light):</b></td></tr>
  
  <tr>
    <td><img src="/test_images/test_1/test_1_light.png" width="200px" height="200px"></td>
    <td><img src="/test_images/test_1/test_nolight.png" width="200px" height="200px"></td>
    <td><img src="/test_images/test_1/test_1_mask.png" width="200px" height="200px"></td>
    <td><img src="/test_images/test_1/Test_1.gif" width="200px" height="200px"></td>
  </tr>

  <tr><td colspan=3><b>Example #2 (two point light):</b></td></tr>
  
  <tr>
    <td><img src="/Tests/test_2_light.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_nolight.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_2_mask.png" width="150px" height="150px"></td>
  </tr>

  <tr><td colspan=3><b>Example #3 (two point light and one spot light):</b></td></tr>
  
  <tr>
    <td><img src="/Tests/test_3_light.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_nolight.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_3_mask.png" width="150px" height="150px"></td>
  </tr>

  <tr><td colspan=3><b>Example #4 (one light, colored meshes and reflactions):</b></td></tr>
  
  <tr>
    <td><img src="/Tests/test_4_light.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_4_nolight.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_4_mask.png" width="150px" height="150px"></td>
  </tr>

  <tr><td colspan=3><b>Example #5:</b></td></tr>
  
  <tr>
    <td><img src="/Tests/test_5_light.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_5_nolight.png" width="150px" height="150px"></td>
    <td><img src="/Tests/test_5_mask_2.png" width="150px" height="150px"></td>
  </tr>
  
  > [!NOTE]
  > All examples were conducted in eevee, I do not know how the program will work with cycles.
</table>


