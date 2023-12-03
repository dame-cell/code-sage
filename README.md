# Quantization 

This conceptual guide gives a brief overview of [Quantization](https://arxiv.org/abs/2103.13630).

In general, quantization can be defined as the process of mapping values from a large set of real numbers to values in a small discrete set. Typically, this involves transforming continuous inputs into fixed values at the output.



Two common ways to achieve this is by:

* Rounding: We compute the nearest integer. For example, a value of 1.8 would be rounded to 2, while a value of 1.2 would be rounded to 1.

* Truncating: We blindly remove the decimal point from a value to convert it to an integer. For instance, 1.23424 would be truncated to 1.


In simpler terms, quantization helps us train big neural networks more efficiently by using less memory. It's like using fewer bits to store information, making things faster and more manageable. For example, instead of using float32 bits, we can use int8 bits, which further reduces the memory footprint while still preserving the essential information.


# Motivation 

Regardless of the quantization method chosen, our main motivation is to achieve the following:

* Improve the Inference speed :  training Deep Neurel Network is computationally very expensive ,with the advent of LLMs , The number of parameters for these models are steadily increasing ,meaning that the memory footprint is getting higher and higher. Here,  Quantization comes to the rescue.

* The need for quantized models : There is increasing demands to run these models on our laptops or small devices such as  mobile phone . 
  
  None of the above is possible without **Quantization**   
  

# Numeric Data Types in Computer Memory

Let's not forget that trained Neurel Networks ,  are just flaoting numbers stored in computer's memory ,Some of the common omes are :

* float32 or fp32 : Floating-point numbers using 32 bits (single-precision floating-point).
* float16 or fp16  : Floating-point numbers using 16 bits (double-precision floating-point).
* float64 or fp64: Floating-point numbers using 64 bits (double-precision floating-point).
* int8: Integer numbers using 8 bits (8-bit integer).
* int16: Integer numbers using 16 bits (16-bit integer).
* int32: Integer numbers using 32 bits (32-bit integer).
* int64: Integer numbers using 64 bits (64-bit integer).


<div class="flex justify-center">
    <img src="!![Screenshot (18)](https://github.com/dame-cell/code-sage/assets/122996026/8b06259f-7ef0-477c-92ea-8daf40107b15)"/>
</div>

