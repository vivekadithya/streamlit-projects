import streamlit as st
import pandas as pd
import altair as alt

st.write("""
         # DNA Count Web Application

         This app counts the nuecleotide composition of query DNA!

         """)

st.header("""
          Enter DNA Sequence
          """)

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # skips the first part of the input string
sequence = "".join(sequence)

st.header("""
          Input DNA Sequence
          """)
sequence_input

st.header("""
          Output DNS Neucleotide Count
          """)

st.subheader("""
             1. Print Dictionary
             """)

# Count the DNA sequences


def dna_sequence_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = dna_sequence_count(sequence)


# Display the counts
st.subheader("Sequence Counts")
st.write(f"There are {str(X['A'])} adenine (A)")
st.write(f"There are {str(X['T'])} thymine (T)")
st.write(f"There are {str(X['G'])} guanine (G)")
st.write(f"There are {str(X['C'])} cytosine (C)")

# display data frame

st.subheader('3. Display Header')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Count'}, axis=1)
df.reset_index(inplace=True)
df = df.rename({'index': 'Nuecleotide'}, axis=1)
st.write(df)

# display bar chart
st.subheader('4. Bar Chart')
plt = alt.Chart(df).mark_bar().encode(
    x='Nuecleotide',
    y='Count',
    color=alt.value('white')
)

plt = plt.properties(
    width=alt.Step(80)  # bar width
)

st.write(plt)
